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
        print('Config regenerated from database...\nStarting to monitor hypervisors changes...')
        for hyper in r.table('hypervisors').pluck('id','vpn').changes(include_initial=False).run():
            if hyper['new_val'] == None:
                ### User was deleted
                print('Hypervisor deleted:')
                wg.remove_peer(hyper['old_val'])
                continue
            if user['old_val'] == None:
                ### New user
                print('New hypervisor '+hyper['new_val']['id']+'found...')
                wg.add_peer(hyper['new_val'])
            else:
                ### Updated vpn user config
                if 'vpn' not in hyper['old_val']: 
                    continue #Was just added

                if hyper['old_val']['vpn']['iptables'] != hyper['new_val']['vpn']['iptables']:
                    print('Modified iptables')
                    wg.set_iptables(hyper['new_val'])
                else:
                    print('Modified user wireguard config')
                    # who else could modify the wireguard config?? 
                    wg.update_peer(hyper['new_val'])

    except ReqlDriverError:
        print('Hypers: Rethink db connection lost!')
        log.error('Hypers: Rethink db connection lost!')
        time.sleep(.5)
    except Exception as e:
        print('Hypers internal error: \n'+traceback.format_exc())
        log.error('Hypers internal error: \n'+traceback.format_exc())
        exit(1)

print('Hypers ENDED!!!!!!!')
log.error('Hypers ENDED!!!!!!!')  