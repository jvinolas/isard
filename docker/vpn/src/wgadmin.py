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
        wg=Wg()

        print('Config regenerated from database...\nStarting to monitor users changes...')
        #for user in r.table('users').pluck('id','vpn').changes(include_initial=False).run():
        for user in r.table('users').pluck('id','vpn').merge({'table':'users'}).changes(include_initial=False).union(
            r.table('hypervisors').pluck('id','vpn').merge({'table':'hypers'}).changes(include_initial=False)).run():
            if user['new_val'] == None:
                ### User was deleted
                print('User deleted:')
                wg.remove_peer(user['old_val'])
                continue
            if user['old_val'] == None:
                ### New user
                print('New user '+user['new_val']['id']+'found...')
                wg.add_peer(user['new_val'])
            else:
                ### Updated vpn user config
                if 'vpn' not in user['old_val']: 
                    continue #Was just added

                if user['old_val']['vpn']['iptables'] != user['new_val']['vpn']['iptables']:
                    print('Modified iptables')
                    wg.set_iptables(user['new_val'])
                else:
                    print('Modified user wireguard config')
                    # who else could modify the wireguard config?? 
                    wg.update_peer(user['new_val'])

    except ReqlDriverError:
        print('Users: Rethink db connection lost!')
        log.error('Users: Rethink db connection lost!')
        time.sleep(.5)
    except Exception as e:
        print('Users internal error: \n'+traceback.format_exc())
        log.error('Users internal error: \n'+traceback.format_exc())
        exit(1)

print('Users ENDED!!!!!!!')
log.error('Users ENDED!!!!!!!')  