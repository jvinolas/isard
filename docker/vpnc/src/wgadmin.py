import os, time
from pprint import pprint
import traceback

from rethinkdb import RethinkDB; r = RethinkDB()
from rethinkdb.errors import ReqlDriverError, ReqlTimeoutError

import logging as log

from subprocess import check_call, check_output

def dbConnect():
    r.connect(host=os.environ['STATS_RETHINKDB_HOST'], port=os.environ['STATS_RETHINKDB_PORT'],db=os.environ['RETHINKDB_DB']).repl()

def get_wireguard_file(peer):
    endpoint=os.environ['STATS_RETHINKDB_HOST']
    try:
        server_public_key=r.db('isard').table('config').get(1).pluck({'vpn_hypers':{'wireguard':{'keys':{'public'}}}}).run()['vpn']['wireguard']['keys']['public']
    except:
        raise
    return """[Interface]
Address = %s
PrivateKey = %s

[Peer]
PublicKey = %s
Endpoint = %s:443
AllowedIPs = %s
PersistentKeepalive = 21
""" % (peer['vpn']['wireguard']['Address'],peer['vpn']['wireguard']['keys']['private'],server_public_key,endpoint,peer['vpn']['wireguard']['AllowedIPs'])

def init_client(peer):
    ## Server config
    try:
        check_output(('/usr/bin/wg-quick', 'down', 'wg0'), text=True).strip()
    except:
        None
    with open("/etc/wireguard/wg0.conf", "w") as f:
        f.write(get_wireguard_file(peer))
    check_output(('/usr/bin/wg-quick', 'up', 'wg0'), text=True).strip()

connection=False
while not connection:
    try:
        dbConnect()
        peer = r.table('hypervisors').get('isard-hypervisor').run()
        if peer != None:
            init_client(peer)
            connection=True
    except ReqlDriverError:
        print('Hypervisors: Rethink db connection lost!')
        log.error('Hypervisors: Rethink db connection lost!')
        time.sleep(5)
    except Exception as e:
        print('Hypervisors internal error: \n'+traceback.format_exc())
        log.error('Hypervisors internal error: \n'+traceback.format_exc())
        exit(1)
        
print('Hypervisors ENDED!!!!!!!')
log.error('Hypervisors ENDED!!!!!!!')  