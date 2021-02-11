# Copyright 2017 the Isard-vdi project authors:
#      Josep Maria Viñolas Auquer
#      Alberto Larraz Dalmases
# License: AGPLv3

#!/usr/bin/env python
# coding=utf-8
import sys, json, os
from webapp import app
import rethinkdb as r
from ..lib.log import * 

from .flask_rethink import RethinkDB
db = RethinkDB(app)
db.init_app(app)

import urllib

class isardVpn():
    def __init__(self):
        pass

    def vpn_data(self,vpn,kind,operating_system,current_user=False, id=False):
        if vpn == 'users':
            if current_user == False: return False
            wgdata = r.table('users').get(current_user.id).pluck('vpn').run(db.conn)
            if app.wireguard_users_keys == False:
                sysconfig = r.db('isard').table('config').get(1).run(db.conn)
                app.wireguard_users_keys = sysconfig.get('vpn_users', {}).get('wireguard', {}).get('keys', False)
            if app.wireguard_users_keys == False:
                log.error('There are no wireguard keys in webapp config yet. Try again in a few seconds...')
                return False
            server_keys = app.wireguard_users_keys
            port=os.environ['WG_USERS_PORT']
        elif vpn == 'hypers':
            if id == False: return False
            wgdata = r.table('hypervisors').get(id).pluck('vpn').run(db.conn)
            if app.wireguard_hypers_keys == False:
                sysconfig = r.db('isard').table('config').get(1).run(db.conn)
                app.wireguard_hypers_keys = sysconfig.get('vpn_hypers', {}).get('wireguard', {}).get('keys', False)
            if app.wireguard_hypers_keys == False:
                log.error('There are no wireguard hypers keys in webapp config yet. Try again in a few seconds...')
                return False
            server_keys = app.wireguard_hypers_keys
            port=os.environ['WG_HYPERS_PORT']
        else:
            return False
        if wgdata == None or 'vpn' not in wgdata.keys():
            return False
        ## First up time the wireguard config keys are missing till isard-vpn populates it.

        endpoints=list(r.table('hypervisors').pluck({'viewer': 'static'}).run(db.conn))
        if len(endpoints):
            endpoint = endpoints[0]['viewer']['static']
        if kind == 'config':
            return {'kind':'file','name':'isard-vpn','ext':'conf','mime':'text/plain','content':self.get_wireguard_file(endpoint,wgdata,server_keys,port)} 
        elif kind == 'install':
            ext='sh' if operating_system == 'Linux' else 'vb'
            return {'kind':'file','name':'isard-vpn-setup','ext':ext,'mime':'text/plain','content':self.get_wireguard_install_script(endpoint,wgdata,os,server_keys,port)} 

        return False
        
    def get_wireguard_file(self,endpoint,peer,server_keys,port):
        if peer['vpn']['wireguard']['extra_client_nets'] != None:
            address=peer['vpn']['wireguard']['Address']+','+peer['vpn']['wireguard']['extra_client_nets']
        else:
            address=peer['vpn']['wireguard']['Address']
        return """[Interface]
Address = %s
PrivateKey = %s

[Peer]
PublicKey = %s
Endpoint = %s:%s
AllowedIPs = %s
PersistentKeepalive = 21
""" % (peer['vpn']['wireguard']['Address'],peer['vpn']['wireguard']['keys']['private'],server_keys['public'],endpoint,port,address)

    def get_wireguard_install_script(self,endpoint,peer,os,server_keys,port):
        return """#!/bin/bash
echo "Installing wireguard. Ubuntu/Debian script."
apt install -y wireguard git dh-autoreconf libglib2.0-dev intltool build-essential libgtk-3-dev libnma-dev libsecret-1-dev network-manager-dev resolvconf
git clone https://github.com/max-moser/network-manager-wireguard
cd network-manager-wireguard
./autogen.sh --without-libnm-glib
./configure --without-libnm-glib --prefix=/usr --sysconfdir=/etc --libdir=/usr/lib/x86_64-linux-gnu --libexecdir=/usr/lib/NetworkManager --localstatedir=/var
make   
sudo make install
cd ..
echo "%s" > isard-vpn.conf
echo "You have your user vpn configuration to use it with NetworkManager: isard-vpn.conf""" % self.get_wireguard_file(endpoint,peer,server_keys,port)