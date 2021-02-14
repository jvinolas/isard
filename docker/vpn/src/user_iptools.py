
from pprint import pprint

import os
from rethinkdb import RethinkDB; r = RethinkDB()
from rethinkdb.errors import ReqlDriverError, ReqlTimeoutError

from subprocess import check_call, check_output
import ipaddress
import traceback

from iptools import IpTools
import iptc

ipt=IpTools()

REJECT={'target': {'REJECT': {'reject-with': 'icmp-host-prohibited'}}}

class UserIpTools(object):
    def __init__(self):
        ipt.flush_chains()

        iptc.easy.add_chain('filter', 'fw-users')
        iptc.easy.insert_rule('filter', 'fw-users', REJECT)

        iptc.easy.add_chain('filter', 'fw-vpn')
        rule={'src':'10.0.0.0/255.255.0.0',
              'target': 'fw-users'}
        iptc.easy.insert_rule('filter', 'fw-vpn', rule)

        #self.add_user('beto')
        pprint(iptc.easy.dump_table('filter', ipv6=False))


    def get_tables(self):
        return iptc.easy.dump_table('filter', ipv6=False)

    def add_user(self,id,src):
        #iptables -A fw-beto -j fw-users
        iptc.easy.add_chain('filter', 'fw-'+id)
        rule={'target': 'fw-'+id}
        iptc.easy.insert_rule('filter', 'fw-users', rule)
        rule={'src':src,
            'target': 'fw-'+id}
        iptc.easy.insert_rule('filter', 'fw-vpn', rule)

        print('user iptables added')
        #iptables -I fw-vpn -s 10.1.2.3 -j fw-beto

    def del_user(self,id,src):
        iptc.easy.delete_chain('filter', 'fw-'+id, flush=True)
        print('user iptables deleted')

    def desktop_add(self,user_id,desktop_ip):
        rule={'dst':desktop_ip,
            'target': 'fw-'+user_id}
        pprint(rule)
        iptc.easy.insert_rule('filter', 'fw-vpn', rule)
        print('desktop iptables added')

    def desktop_remove(self,user_id,desktop_ip):
        rule={'dst':desktop_ip,
            'target': 'fw-'+user_id}
        pprint(rule)
        iptc.easy.insert_rule('filter', 'fw-vpn', rule)
        print('desktop iptables deleted')

test=UserIpTools()
