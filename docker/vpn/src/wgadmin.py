import os, time
from pprint import pprint
import traceback

from rethinkdb import RethinkDB; r = RethinkDB()
from rethinkdb.errors import ReqlDriverError, ReqlTimeoutError

import logging as log

from wgtools import Wg


def dbConnect():
    r.connect(host=os.environ['RETHINKDB_HOST'], port=os.environ['RETHINKDB_PORT'],db=os.environ['RETHINKDB_DB']).repl()

while True:
    try:
        # App was restarted or db was lost. Just sync peers before get into changes.
        print('Checking initial config...')
        dbConnect()
        wg_users=Wg(interface='users',clients_net=os.environ['WG_USERS_NET'],table='users',server_port=os.environ['WG_USERS_PORT'],allowed_client_nets=os.environ['WG_HYPER_GUEST_SUPERNET'])
        wg_hypers=Wg(interface='hypers',clients_net=os.environ['WG_HYPERS_NET'],table='hypervisors',server_port=os.environ['WG_HYPERS_PORT'],allowed_client_nets=os.environ['WG_HYPER_NET'])

        print('Config regenerated from database...\nStarting to monitor users changes...')
        #for user in r.table('users').pluck('id','vpn').changes(include_initial=False).run():
        for user in r.table('users').pluck('id','vpn').merge({'table':'users'}).changes(include_initial=False).union(
            r.table('hypervisors').pluck('id','vpn').merge({'table':'hypers'}).changes(include_initial=False)).run():
            if user['new_val'] == None:
                ### User was deleted
                print('Deleted:')
                if data['old_val']['table'] == 'users':
                    wg_users.remove_peer(data['old_val'])
                else:
                    wg_hypers.remove_peer(data['old_val'])
                continue
            if user['old_val'] == None:
                ### New user
                print('New: '+data['new_val']['id']+'found...')
                if data['old_val']['table'] == 'users':
                    wg_users.add_peer(data['new_val'])
                else:
                    wg_hypers.add_peer(data['new_val'])
            else:
                ### Updated vpn data config
                if 'vpn' not in data['old_val']: 
                    continue #Was just added

                if user['old_val']['vpn']['iptables'] != data['new_val']['vpn']['iptables']:
                    print('Modified iptables')
                    if data['old_val']['table'] == 'users':
                        wg_users.set_iptables(data['new_val'])
                    else:
                        wg_hypers.set_iptables(data['new_val'])
                else:
                    print('Modified user wireguard config')
                    # who else could modify the wireguard config?? 
                    if data['old_val']['table'] == 'users':
                        wg_users.update_peer(data['new_val'])
                    else:
                        wg_hypers.update_peer(data['new_val'])

    except ReqlDriverError:
        print('Users: Rethink db connection lost!')
        log.error('Users: Rethink db connection lost!')
        time.sleep(.5)
    except Exception as e:
        print('Users internal error: \n'+traceback.format_exc())
        log.error('Users internal error: \n'+traceback.format_exc())
        exit(1)

print('Thread ENDED!!!!!!!')
log.error('Thread ENDED!!!!!!!')  