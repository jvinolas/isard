
from pprint import pprint

import os
from rethinkdb import RethinkDB; r = RethinkDB()
from rethinkdb.errors import ReqlDriverError, ReqlTimeoutError

from subprocess import check_call, check_output
import ipaddress

class Keys(object):
    def __init__(self):
        self.wg = '/usr/bin/wg'
        self.skeys={'private':False, 'public':False}
        self.update_clients=False
        self.check_server_cert()

    def gen_private_key(self):
        return check_output((self.wg, 'genkey'), text=True).strip()

    def gen_public_key(self, private_key):
        return check_output((self.wg, 'pubkey'), input=private_key, text=True).strip()  

    def gen_server_keys(self):
        ## Private goes in wg0.conf [Interface] config
        self.skeys['private']=self.gen_private_key()
        ## Public goes in all client config [Peer]
        self.skeys['public']=self.gen_public_key(self.skeys['private'])     

    def new_client_keys(self):
        private=self.gen_private_key()
        return {'private':private,
                'public':self.gen_public_key(private)}

    def gen_presharedkey(self):
        return check_output((self.wg, 'genpsk'), text=True).strip()

    def check_server_cert(self):
        # Check old server key with new server key that matches.
        # If new key found then all client keys should be updated!
        update_clients=False

        try:
            with open("/certs/server_private.key", "r") as f:
                actual_private_key=f.read()
            with open("/certs/server_public.key", "r") as f:
                actual_public_key=f.read()
        except FileNotFoundError:
            self.gen_server_keys()
            actual_private_key=self.skeys['private']
            actual_public_key=self.skeys['public']
            ## Generate new ones
        except Exception as e:
            print('Serve read keys error: \n'+traceback.format_exc())
            log.error('Server read keys internal error: \n'+traceback.format_exc())
            exit(1)

        old_key=r.table('config').get(1).pluck('vpn').run()

        if 'vpn' not in old_key.keys() or actual_private_key != old_key['vpn']['wireguard']['keys']['private']:
            r.table('config').get(1).update({'vpn':{'wireguard':{'keys':{'private':actual_private_key,
                                                                        'public':actual_public_key}}}}).run()
            update_clients=True
            try:
                with open("/certs/server_private.key", "w") as f:
                    f.write(actual_private_key)
                with open("/certs/server_public.key", "w") as f:
                    f.write(actual_public_key)
            except Exception as e:
                print('Serve keys write error: \n'+traceback.format_exc())
                log.error('Server write keys internal error: \n'+traceback.format_exc())    
                exit(1)            
        self.skeys={'private':actual_private_key,
                    'public':actual_public_key}
        self.update_clients=update_clients

        
class Wg(object):

    def __init__(self):
        # Get actual server keys or generate new ones
        self.keys=Keys()

        self.server_mask=os.environ['WG_CLIENTS_NET'].split('/')[1]
        self.server_net=ipaddress.ip_network(os.environ['WG_CLIENTS_NET'], strict=False)
        # Get first one from range for us!
        self.server_ip=str(self.server_net[1])

        self.clients_reserved_ips=[self.server_ip]
        # Get existing users wireguard config and generate new one's if not exist.
        self.init_server()
        self.init_peers()
        #for user_id,peer in self.peers.items():
        #    print(self.client_config(peer))

    def init_server(self):
        ## Server config
        try:
            check_output(('/usr/bin/wg-quick', 'down', 'wg0'), text=True).strip()
        except:
            None
        self.config=self.server_config()
        #for k,v in self.peers.items():
        #    self.set_iptables(v)
        #    self.config=self.config+self.gen_peer_config(v)
        with open("/etc/wireguard/wg0.conf", "w") as f:
            f.write(self.config)
        check_output(('/usr/bin/wg-quick', 'up', 'wg0'), text=True).strip()
        ## End server config

    def init_peers(self):
        # This will reset all vpn config on restart.
        r.table('users').replace(r.row.without('vpn')).run()
        r.table('hypervisors').replace(r.row.without('vpn')).run()

        vpn_tables = ['hypervisors','users']
        wglist_tables={}
        for table in vpn_tables:
            wglist_tables[table] = list(r.table(table).pluck('id','vpn').run())
            self.clients_reserved_ips=self.clients_reserved_ips+[p['vpn']['wireguard']['Address'] for p in wglist_tables[table] if 'vpn' in p.keys() and 'wireguard' in p['vpn'].keys()]

        for table in vpn_tables:
            wglist = wglist_tables[table]
            create_peers=[]
            if self.keys.update_clients == True:
                print('Server key changed. Generating new client keys for all users...')
            for peer in wglist:
                new_peer=False
                if self.keys.update_clients == True and 'vpn' in peer.keys() and 'wireguard' in peer['vpn'].keys():
                    new_peer=peer
                    new_peer['vpn']['wireguard']['keys']=self.keys.new_client_keys()
                    create_peers.append(new_peer)
                if 'vpn' not in peer.keys():
                    new_peer=self.gen_new_peer(peer)
                    create_peers.append(new_peer)
                if new_peer == False:
                    self.up_peer(peer)
                else:
                    self.up_peer(new_peer)
            pprint(create_peers)
            r.table(table).insert(create_peers, conflict='update').run()

    def gen_new_peer(self,peer):
        return {'id':peer['id'],
                'vpn':{ 'iptables':[],
                        'wireguard':
                            {'Address':self.gen_client_ip(),
                            'keys':self.keys.new_client_keys(),
                            'AllowedIPs':'0.0.0.0/0'}}} 

    def up_peer(self,peer):
        check_output(('/usr/bin/wg', 'set', 'wg0', 'peer', peer['vpn']['wireguard']['keys']['public'], 'allowed-ips', peer['vpn']['wireguard']['Address']), text=True).strip()  

    def add_peer(self,peer):
        new_peer = self.gen_new_peer(peer)
        self.up_peer(new_peer)
        r.table('users').insert(new_peer, conflict='update').run()


    def remove_peer(self,peer):
        if 'vpn' in peer.keys() and 'wireguard' in peer['vpn'].keys():
            check_output(('/usr/bin/wg', 'set', 'wg0', 'peer', peer['vpn']['wireguard']['keys']['public'], 'remove'), text=True).strip()  


    def gen_client_ip(self):
        next_ip = str(next(host for host in self.server_net.hosts() if str(host) not in self.clients_reserved_ips))
        self.clients_reserved_ips.append(next_ip)
        return next_ip
 
    def gen_peer_config(self,peer):
        #allowed_ips=','.join(peer['vpn']['wireguard']['AllowedIPs'])
        return '[peer]\nPublicKey='+peer['vpn']['wireguard']['keys']['public']+'\nAllowedIPs='+peer['vpn']['wireguard']['Address']+'\n\n'

    def set_iptables(self,peer):
        iptables=peer['vpn']['iptables']

    def server_config(self):
        return """[Interface]
Address = %s
SaveConfig = false
PrivateKey = %s
ListenPort = 443
PostUp = iptables -I FORWARD -i wg0 -o wg0 -j REJECT --reject-with icmp-host-prohibited

""" % (self.server_ip,self.keys.skeys['private'])





    def client_config(self,peer):
        return """[Interface]
Address = %s
PrivateKey = %s

[Peer]
PublicKey = %s
Endpoint = server:443
AllowedIPs = 192.168.128.0/22
PersistentKeepalive = 21
""" % (peer['vpn']['wireguard']['AllowedIPs'],peer['vpn']['wireguard']['keys']['private'],self.keys.skeys['public'])

