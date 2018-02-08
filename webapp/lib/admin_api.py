# Copyright 2017 the Isard-vdi project authors:
#      Josep Maria Viñolas Auquer
#      Alberto Larraz Dalmases
# License: AGPLv3

#!/usr/bin/env python
# coding=utf-8
import time
from webapp import app
from werkzeug import secure_filename

from datetime import datetime, timedelta
import requests, socket
# ~ import itertools
import pprint
import tarfile,pickle,os
# ~ import subprocess
from contextlib import closing
    
import rethinkdb as r

from ..lib.log import * 

from .flask_rethink import RethinkDB
db = RethinkDB(app)
db.init_app(app)

from ..auth.authentication import Password

class isardAdmin():
    def __init__(self):
        self.f=flatten()


    def check(self,dict,action):
        #~ These are the actions:
        #~ {u'skipped': 0, u'deleted': 1, u'unchanged': 0, u'errors': 0, u'replaced': 0, u'inserted': 0}
        if dict[action] or dict['unchanged']: 
            return True
        if not dict['errors']: return True
        return False

    def getUnflatten(self,dict):
        f=flatten()
        return f.unflatten_dict(dict)
        
    def check_socket(host, port):
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            if sock.connect_ex((host, port)) == 0:
                return True
            else:
                return False
                    
    '''
    ADMIN API
    '''
    def delete_table_key(self,table,key):
        with app.app_context():
            return self.check(r.table(table).get(key).delete().run(db.conn),'deleted')

    def multiple_action(self, table, action, ids):
        with app.app_context():
            if action == 'toggle':
                domains_stopped=self.multiple_check_field(table,'status','Stopped',ids)
                domains_started=self.multiple_check_field(table,'status','Started',ids)
                res_stopped=r.table(table).get_all(r.args(domains_stopped)).update({'status':'Starting'}).run(db.conn)
                res_started=r.table(table).get_all(r.args(domains_started)).update({'status':'Stopping'}).run(db.conn)
                return True
            if action == 'delete':
                domains_deleting=self.multiple_check_field(table,'status','Deleting',ids)
                res=r.table(table).get_all(r.args(domains_deleting)).delete().run(db.conn) 
                                
                domains_stopped=self.multiple_check_field(table,'status','Stopped',ids)
                res=r.table(table).get_all(r.args(domains_stopped)).update({'status':'Deleting'}).run(db.conn)
                domains_disabled=self.multiple_check_field(table,'status','Disabled',ids)
                res=r.table(table).get_all(r.args(domains_disabled)).update({'status':'Deleting'}).run(db.conn)                
                domains_failed=self.multiple_check_field(table,'status','Failed',ids)
                res=r.table(table).get_all(r.args(domains_failed)).update({'status':'Deleting'}).run(db.conn) 
                domains_creating=self.multiple_check_field(table,'status','Creating',ids)
                res=r.table(table).get_all(r.args(domains_creating)).update({'status':'Deleting'}).run(db.conn)                                              
                domains_creatingdisk=self.multiple_check_field(table,'status','CreatingDisk',ids)
                res=r.table(table).get_all(r.args(domains_creatingdisk)).update({'status':'Deleting'}).run(db.conn) 
                domains_creatingstarting=self.multiple_check_field(table,'status','CreatingAndStarting',ids)
                res=r.table(table).get_all(r.args(domains_creatingstarting)).update({'status':'Deleting'}).run(db.conn) 
                return True
            if action == 'force_failed':
                res_deleted=r.table(table).get_all(r.args(ids)).update({'status':'Failed'}).run(db.conn)
                return True
            if action == 'force_stopped':
                res_deleted=r.table(table).get_all(r.args(ids)).update({'status':'Stopped'}).run(db.conn)
                return True
            if action == "stop_noviewer":
                domains_tostop=self.multiple_check_field(table,'status','Started',ids)
                res=r.table(table).get_all(r.args(domains_tostop)).filter(~r.row.has_fields({'viewer':'client_since'})).update({'status':'Stopping'}).run(db.conn)
                return True
                
    def multiple_check_field(self, table, field, value, ids):
        with app.app_context():
            return [d['id'] for d in list(r.table(table).get_all(r.args(ids)).filter({field:value}).pluck('id').run(db.conn))]

    def get_admin_table(self, table, pluck=False, id=False, order=False, flatten=True):
        with app.app_context():
            if id and not pluck:
                data=r.table(table).get(id).run(db.conn)
                return self.f.flatten_dict(data) if flatten else data
            if pluck and not id:
                if order:
                    data=r.table(table).order_by(order).pluck(pluck).run(db.conn)
                    return self.f.table_values_bstrap(data) if flatten else list(data)
                else:
                    data=r.table(table).pluck(pluck).run(db.conn)
                    return self.f.table_values_bstrap(data) if flatten else list(data)
            if pluck and id:
                data=r.table(table).get(id).pluck(pluck).run(db.conn)
                return self.f.flatten_dict(data) if flatten else data
            if order:
                data=r.table(table).order_by(order).run(db.conn)
                return self.f.table_values_bstrap(data) if flatten else list(data)
            else:
                data=r.table(table).run(db.conn)
                return self.f.table_values_bstrap(data) if flatten else list(data)

    def get_admin_table_term(self, table, field, value, pluck=False):
        with app.app_context():
            if pluck:
                return self.f.table_values_bstrap(r.table(table).filter(lambda doc: doc[field].match('(?i)'+value)).pluck(pluck).run(db.conn))
            else:
                return self.f.table_values_bstrap(r.table(table).filter(lambda doc: doc[field].match('(?i)'+value)).run(db.conn))

    def insert_table_dict(self, table, dict):
        with app.app_context():
            return self.check(r.table(table).insert(dict).run(db.conn), 'inserted')

    def insert_or_update_table_dict(self, table, dict):
        with app.app_context():
            return r.table(table).insert(dict, conflict='update').run(db.conn)
                                        
    def update_table_dict(self, table, id, dict):
        with app.app_context():
            return self.check(r.table(table).get(id).update(dict).run(db.conn), 'replaced')
            
    '''
    USERS
    '''
    def user_add(self,user):
        # ~ d': 'prova', 'password': 'prova', 'name': 'prova', 
        # ~ 'quota': {'hardware': {'vcpus': 1, 'memory': 1000}, 
        # ~ 'domains': {'templates': 1, 'running': 1, 'isos': 1, 'desktops': 1}}}
        p = Password()
        usr = {'kind': 'local',
               'active': True,
                'accessed': time.time(),
                'password': p.encrypt(user['password'])}
        del user['password']
        user={**usr, **user}
        
        for k,v in user['quota']['domains'].items():
            user['quota']['domains'][k]=int(v)
        for k,v in user['quota']['hardware'].items():
            user['quota']['hardware'][k]=int(v)     
                    
        qdomains ={'desktops_disk_max': 99999999,  # 100GB
                    'templates_disk_max': 99999999,
                    'isos_disk_max': 99999999}
        user['quota']['domains']={**qdomains, **user['quota']['domains']}       
        return self.check(r.table('users').insert(user).run(db.conn),'inserted')

    def users_add(self,users):
        # ~ d': 'prova', 'password': 'prova', 'name': 'prova', 
        # ~ 'quota': {'hardware': {'vcpus': 1, 'memory': 1000}, 
        # ~ 'domains': {'templates': 1, 'running': 1, 'isos': 1, 'desktops': 1}}}
        p = Password()
        final_users=[]
        for user in users:
            
            usr = {'kind': 'local',
                   'active': True,
                    'accessed': time.time(),
                    'password': p.encrypt(user['password'])}
            # ~ usr['id']=user['username']
            del user['password']
            user={**usr, **user}
            
            for k,v in user['quota']['domains'].items():
                user['quota']['domains'][k]=int(v)
            for k,v in user['quota']['hardware'].items():
                user['quota']['hardware'][k]=int(v)  
                        
            qdomains ={'desktops_disk_max': 99999999,  # 100GB
                        'templates_disk_max': 99999999,
                        'isos_disk_max': 99999999}
            user['quota']['domains']={**qdomains, **user['quota']['domains']}
            
            final_users.append(user)          
        return self.check(r.table('users').insert(final_users).run(db.conn),'inserted')

    def user_edit(self,user):
        # ~ d': 'prova', 'password': 'prova', 'name': 'prova', 
        # ~ 'quota': {'hardware': {'vcpus': 1, 'memory': 1000}, 
        # ~ 'domains': {'templates': 1, 'running': 1, 'isos': 1, 'desktops': 1}}}
        p = Password()
        usr = {'kind': 'local',
               'active': True,
                'accessed': time.time()}
        user={**usr, **user}
        
        for k,v in user['quota']['domains'].items():
            user['quota']['domains'][k]=int(v)
        for k,v in user['quota']['hardware'].items():
            user['quota']['hardware'][k]=int(v)  
                    
        qdomains ={'desktops_disk_max': 99999999,  # 100GB
                    'templates_disk_max': 99999999,
                    'isos_disk_max': 99999999}
        user['quota']['domains']={**qdomains, **user['quota']['domains']}
        return self.check(r.table('users').update(user).run(db.conn),'replaced')

    def user_toggle_active(self,id):
        with app.app_context():
            is_active = not r.table('users').get(id).pluck('active').run(db.conn)['active'] 
            if is_active:
                r.table('domains').get_all(id, index='user').filter({'kind':'desktop','status':'Disabled'}).update({'status':'Stopped'}).run(db.conn)
            else:
                r.table('domains').get_all(id, index='user').filter({'kind':'desktop'}).update({'status':'Disabled'}).pluck('id').run(db.conn)
            return self.check(r.table('users').get(id).update({'active':is_active}).run(db.conn),'replaced')

                    
    def get_admin_user(self):
        with app.app_context():
            ## ALERT: Should remove password (password='')
            return self.f.table_values_bstrap(r.table('users').run(db.conn))

    def get_admin_users_domains(self):
        with app.app_context():
            # ~ desk=list(r.table('domains').get_all('desktop', index='kind').run(db.conn))
            # ~ print(len([d['id'] for d in desk if d['user']=='jvinolas' ]))
            # ~ pub=r.table('domains').get_all('public_template', index='kind').run(db.conn)
            # ~ priv=r.table('domains').get_all('user_template', index='kind').run(db.conn)
            # ~ base=r.table('domains').get_all('base', index='kind').run(db.conn)
            return self.f.table_values_bstrap(
                r.table("users").merge(lambda user:
                    {
                        # This order query never ends
                        # ~ "desktops": r.table("domains").get_all('desktop', index='kind').filter({'user': user['id']}).count(),
                        # ~ "public_template": r.table("domains").get_all('public_template', index='kind').filter({'user': user['id']}).count(),
                        # ~ "user_template": r.table("domains").get_all('user_template', index='kind').filter({'user': user['id']}).count(),
                        # ~ "base": r.table("domains").get_all('base', index='kind').filter({'user': user['id']}).count()
        
                        "desktops": r.table("domains").get_all(user['id'], index='user').filter({'kind': 'desktop'}).count(),
                        "public_template": r.table("domains").get_all(user['id'], index='user').filter({'kind': 'public_template'}).count(),
                        "user_template": r.table("domains").get_all(user['id'], index='user').filter({'kind': 'user_template'}).count(),
                        "base": r.table("domains").get_all(user['id'], index='user').filter({'kind': 'base'}).count()
                    }
                ).run(db.conn))

    def user_delete_checks(self,user_id):
        with app.app_context():
            # User desktops can be deleted, ok?
            user_desktops = list(r.table("domains").get_all(user_id, index='user').filter({'kind': 'desktop'}).pluck('id','name','user',{'create_dict':{'origin'}}).run(db.conn))
            
            # User templates... depending. Are they owned by himself only? Or they have other user derivates??
            user_templates = list(r.table("domains").get_all(r.args(['base','public_template','user_template']),index='kind').filter({'user':user_id}).pluck('id','name','user',{'create_dict':{'origin'}}).run(db.conn))
            risky_templates=[]
            others_domains=0
            for t in user_templates:
                all_template_derivates = self.domain_derivates_count(t['id'])
                usr_template_derivates = self.domain_derivates_count(t['id'],user_id)
                if all_template_derivates != usr_template_derivates:
                    # We've got a problem. There are templates owned by other users. We can't delete this user!
                    t['other_users_derivates']=all_template_derivates - usr_template_derivates
                    risky_templates.append(t)
                    others_domains+=all_template_derivates - usr_template_derivates
        return {'desktops':user_desktops,
                'templates':user_templates,
                'risky_templates':risky_templates,
                'others_domains':others_domains}
                    
    def rcg_add(self,dict):
        table=dict['table']
        dict.pop('table',None)
        dict['id']=app.isardapi.parse_string(dict['name'])
        for k,v in dict['quota']['domains'].items():
            dict['quota']['domains'][k]=int(v)
        for k,v in dict['quota']['hardware'].items():
            dict['quota']['hardware'][k]=int(v)            
        qdomains ={'desktops_disk_max': 99999999,  # 100GB
                    'templates_disk_max': 99999999,
                    'isos_disk_max': 99999999}
        dict['quota']['domains']={**dict['quota']['domains'], **qdomains}       
        return self.check(r.table(table).insert(dict).run(db.conn),'inserted')

    '''
    DOMAINS
    '''
                                
    #~ def get_admin_domains(self,kind=False):
        #~ with app.app_context():
            #~ if not kind:
                #~ return self.f.table_values_bstrap(r.table('domains').without('xml','hardware','create_dict').run(db.conn))
            #~ else:
                 #~ return self.f.table_values_bstrap(r.table('domains').get_all(kind,index='kind').without('xml','hardware','create_dict').run(db.conn))

    def get_admin_domains_with_derivates(self,id=False,kind=False):
        with app.app_context():
            if 'template' in kind:
                if not id:
                    return list(r.table("domains").get_all(r.args(['public_template','user_template']),index='kind').without('xml','hardware','history_domain').merge(lambda domain:
                        {
                            "derivates": r.table('domains').filter({'create_dict':{'origin':domain['id']}}).count()
                        }
                    ).run(db.conn))
                if id:
                    return list(r.table("domains").get(id).without('xml','hardware','history_domain').merge(lambda domain:
                        {
                            "derivates": r.table('domains').filter({'create_dict':{'origin':domain['id']}}).count()
                        }
                    ).run(db.conn))
            elif kind == 'base':
                if not id:
                    return list(r.table("domains").get_all(kind,index='kind').without('xml','hardware','history_domain').merge(lambda domain:
                        {
                            "derivates": r.table('domains').filter({'create_dict':{'origin':domain['id']}}).count()
                        }
                    ).run(db.conn))
                if id:
                    return list(r.table("domains").get(id).without('xml','hardware','history_domain').merge(lambda domain:
                        {
                            "derivates": r.table('domains').filter({'create_dict':{'origin':domain['id']}}).count()
                        }
                    ).run(db.conn))                
            else:
               return list(r.table("domains").get_all(kind,index='kind').without('xml','hardware').merge(lambda domain:
                    {
                        #~ "derivates": r.table('domains').filter({'create_dict':{'origin':domain['id']}}).count(),
                        "accessed": domain['history_domain'][0]['when'].default(0)
                            #~ domain['history_domain'].default('0') | 0
                            #~ domain['history_domain'][0]['when'].default(0)
                    }
                ).run(db.conn))



    def domain_derivates_count(self,id=False,username=False):
        with app.app_context():
            if username is False:
                domains= [ {'id':d['id'],'origin':(d['create_dict']['origin'] if 'create_dict' in d and 'origin' in d['create_dict'] else None)}
                            for d in list(r.table('domains').pluck('id',{'create_dict':{'origin'}}).run(db.conn)) ] 
            else:
                domains= [ {'id':d['id'],'origin':(d['create_dict']['origin'] if 'create_dict' in d and 'origin' in d['create_dict'] else None)}
                            for d in list(r.table('domains').get_all(username, index='user').pluck('id','user',{'create_dict':{'origin'}}).run(db.conn)) ] 
            return self.domain_recursive_count(id,domains)-1


    def domain_recursive_count(self,id,domains):
        # ~ if count == 0:
            # ~ return 0
        count = 1
        # ~ level = 1
        # ~ hierarchy = {}
        doms= [d for d in domains if d['origin']==id]
        for dom in doms:
            # ~ level+=1
            # ~ hierarchy[level]=doms
            count+= self.domain_recursive_count(dom['id'],domains)
        # ~ pprint.pprint(hierarchy)
        return count



    
    def domains_stop(self,hyp_id=False,without_viewer=True):
        with app.app_context():
            try:
                if without_viewer:
                    if hyp_id is False:
                        return r.table('domains').get_all('Started',index='status').filter({'viewer':{'client_since':False}}).update({'status':'Stopping'}).run(db.conn)['replaced']
                    else:
                        return r.table('domains').get_all('Started',index='status').filter({'hyp_started':hyp_id,'viewer':{'client_since':False}}).update({'status':'Stopping'}).run(db.conn)['replaced']
                else:
                    if hyp_id is False:
                        return r.table('domains').get_all('Started',index='status').update({'status':'Stopping'}).run(db.conn)['replaced']
                    else:
                        return r.table('domains').get_all('Started',index='status').filter({'hyp_started':hyp_id}).update({'status':'Stopping'}).run(db.conn)['replaced']
                    
            except:
                return False
                
    def get_admin_templates(self,term):
        with app.app_context():
            data1 = r.table('domains').get_all('base', index='kind').filter(r.row['name'].match(term)).order_by('name').pluck({'id','name','kind','group','icon','user','description'}).run(db.conn)
            data2 = r.table('domains').filter(r.row['kind'].match("template")).filter(r.row['name'].match(term))    .order_by('name').pluck({'id','name','kind','group','icon','user','description'}).run(db.conn)
        return data1+data2
            
    def get_admin_domain_datatables(self):
        with app.app_context():
            return {'columns':self.f.table_header_bstrap('domains'), 'data': self.f.table_values_bstrap('domains', fields)}


    def get_admin_networks(self):
        with app.app_context():
            return list(r.table('interfaces').order_by('name').run(db.conn))

    '''
    HYPERVISORS
    '''
    def hypervisors_get(self, id=False):
        with app.app_context():
            if id:
                flat_dict_list = self.f.flatten_dict(r.table("hypervisors").get(id).merge(lambda hyp:
                                    {
                                        "started_domains": r.table('domains').get_all('Started', index='status').filter({'hyp_started':hyp['id']}).count()
                                    }
                                ).run(db.conn))
            else:
                flat_dict_list = self.f.table_values_bstrap(r.table("hypervisors").merge(lambda hyp:
                                {
                                    "started_domains": r.table('domains').get_all('Started', index='status').filter({'hyp_started':hyp['id']}).count()
                                }
                            ).run(db.conn))
        return flat_dict_list

    def hypervisors_pools_get(self, flat=True):
        with app.app_context():
            if flat:
                return self.f.table_values_bstrap(r.table('hypervisors_pools').run(db.conn))
            else:
                return list(r.table('hypervisors_pools').run(db.conn))
                            
    def hypervisor_toggle_enabled(self,id):
        with app.app_context():
            is_enabled = r.table('hypervisors').get(id).pluck('enabled').run(db.conn)['enabled']
            started_domains = r.table('domains').get_all('Started', index='status').filter({'hyp_started':id}).count()

            if started_domains==0 :            
                status=not is_enabled
                return self.check(r.table('hypervisors').get(id).update({'enabled':status}).run(db.conn),'replaced')
            
            else:
                return False
                
    def hypervisor_add(self,dict):
        with app.app_context():
            if dict['capabilities']['disk_operations']:
                id=dict['id']
                cap_disk=dict['capabilities']['disk_operations']
                cap_hyp=dict['capabilities']['hypervisor']
                for hp in dict['hypervisors_pools']:
                    paths=r.table('hypervisors_pools').get(hp).run(db.conn)['paths']
                    for p in paths:
                        path_list=[]
                        for i,path_data in enumerate(paths[p]):
                            if id not in path_data['disk_operations']:
                                path_data['disk_operations'].append(id)
                                paths[p][i]['disk_operations']=path_data['disk_operations']
                # ~ import pprint
                # ~ pprint.pprint(dict)
                    r.table('hypervisors_pools').get(hp).update({'paths':paths,'enabled':False}).run(db.conn)
            return self.check(r.table('hypervisors').insert(dict).run(db.conn),'inserted')

    def hypervisor_pool_add(self,dict):
        with app.app_context():
            return self.check(r.table('hypervisors_pools').insert(dict).run(db.conn),'inserted')

    def hypervisor_edit(self,dict):
        with app.app_context():
            old_hyp=r.table('hypervisors').get(dict['id']).run(db.conn)
            if not (old_hyp['status']=='Offline' or old_hyp['status']=='Error'): return False
            if old_hyp['capabilities']['disk_operations'] and not dict['capabilities']['disk_operations']:
                # We should remove it from pool. It is not going to be a disk op anymore!
                id=dict['id']
                for hp in dict['hypervisors_pools']:
                    paths=r.table('hypervisors_pools').get(hp).run(db.conn)['paths']
                    for p in paths:
                        path_list=[]
                        for i,path_data in enumerate(paths[p]):
                            if id in path_data['disk_operations']:
                                path_data['disk_operations'].remove(id)
                                paths[p][i]['disk_operations']=path_data['disk_operations']
                    r.table('hypervisors_pools').get(hp).update({'paths':paths}).run(db.conn)                
            
            
            if dict['capabilities']['disk_operations'] and not old_hyp['capabilities']['disk_operations']:
                # It was't a disk op, but now it will
                id=dict['id']
                for hp in dict['hypervisors_pools']:
                    paths=r.table('hypervisors_pools').get(hp).run(db.conn)['paths']
                    for p in paths:
                        path_list=[]
                        for i,path_data in enumerate(paths[p]):
                            if id not in path_data['disk_operations']:
                                path_data['disk_operations'].append(id)
                                paths[p][i]['disk_operations']=path_data['disk_operations']
                    r.table('hypervisors_pools').get(hp).update({'paths':paths,'enabled':False}).run(db.conn)
            return self.check(r.table('hypervisors').update(dict).run(db.conn),'replaced')


    def hypervisor_delete(self,id):
        with app.app_context():
            started_domains = r.table('domains').get_all('Started', index='status').filter({'hyp_started':id}).count()
            if started_domains==0:
                dict=r.table('hypervisors').get(id).run(db.conn)
                if dict['status']=='Deleting':
                    r.table('hypervisors_events').filter({'hyp_id':id}).delete().run(db.conn)
                    r.table('hypervisors_status').filter({'hyp_id':id}).delete().run(db.conn)
                    r.table('hypervisors_status_history').filter({'hyp_id':id}).delete().run(db.conn)
                    
                    if dict['capabilities']['disk_operations']:
                        # ~ id=dict['id']
                        cap_disk=dict['capabilities']['disk_operations']
                        cap_hyp=dict['capabilities']['hypervisor']
                        for hp in dict['hypervisors_pools']:
                            paths=r.table('hypervisors_pools').get(hp).run(db.conn)['paths']
                            for p in paths:
                                path_list=[]
                                for i,path_data in enumerate(paths[p]):
                                    if id in path_data['disk_operations']:
                                        path_data['disk_operations'].remove(id)
                                        paths[p][i]['disk_operations']=path_data['disk_operations']
                            r.table('hypervisors_pools').get(hp).update({'paths':paths}).run(db.conn)
                    return self.check(r.table('hypervisors').get(id).delete().run(db.conn),'deleted')
                else:
                    app.adminapi.update_table_dict('hypervisors',id,{'enabled':False,'status':'Deleting'})
                    return True
            else:
                return False
                

    def get_admin_config(self, id=None):
        with app.app_context():
            if id is None:
                return self.f.flatten_dict(r.table('config').get(1).run(db.conn))
            else:
                return self.f.flatten_dict(r.table('config').get(1).run(db.conn))
                


    '''
    MEDIA
    '''
    def media_add(self,username,partial_dict):
        try:
            partial_dict['url-web']=partial_dict['url']
            del partial_dict['url']
            # ~ filename = partial_dict['url-web'].split('/')[-1]
            user_data=app.isardapi.user_relative_media_path( username, partial_dict['name'])
            partial_dict={**partial_dict, **user_data}
            missing_keys={  'accessed': time.time(),
                            'detail': 'User added',
                            'icon': 'fa-circle-o' if partial_dict['kind']=='iso' else 'fa-floppy-o',
                            'progress': {
                                "received":  "0" ,
                                "received_percent": 0 ,
                                "speed_current":  "" ,
                                "speed_download_average":  "" ,
                                "speed_upload_average":  "" ,
                                "time_left":  "" ,
                                "time_spent":  "" ,
                                "time_total":  "" ,
                                "total":  "" ,
                                "total_percent": 0 ,
                                "xferd":  "0" ,
                                "xferd_percent":  "0"
                                },
                            'status': 'DownloadStarting',
                            'url-isard': False,
                            }
            dict={**partial_dict, **missing_keys}
            return self.insert_table_dict('media',dict)
        except Exception as e:
            log.error('Exception error on media add')
            return False
        return False


    def media_domains_used():
        return list(r.table('domains').filter(
                lambda dom: 
                    (r.args(dom['create_dict']['hardware']['isos'])['id'].eq(id) | r.args(dom['create_dict']['hardware']['floppies'])['id'].eq(id))
                ).run(conn))
        # ~ return list(r.table("domains").filter({'create_dict':{'hardware':{'isos':id}}).pluck('id').run(db.conn))                    
    
    '''
    BACKUP & RESTORE
    '''
    def backup_db(self):
        id='isard_backup_'+datetime.now().strftime("%Y%m%d-%H%M%S")
        path='./backups/'
        os.makedirs(path,exist_ok=True)
        dict={'id':id,
              'filename':id+'.tar.gz',
              'path':path,
              'description':'',
              'when':time.time(),
              'data':{},
              'status':'Initializing'}
        with app.app_context():
            r.table('backups').insert(dict).run(db.conn)
        skip_tables=['backups','domains_status','hypervisors_events','hypervisors_status','domains_status_history','hypervisors_status_history','disk_operations']
        isard_db={}
        with app.app_context():
            r.table('backups').get(id).update({'status':'Loading tables'}).run(db.conn)
            for table in r.table_list().run(db.conn):
                if table not in skip_tables:
                    isard_db[table]=list(r.table(table).run(db.conn))
                    dict['data'][table]=r.table(table).info().run(db.conn)
                    r.table('backups').get(id).update({'data':{table:r.table(table).count().run(db.conn)}}).run(db.conn)
        with app.app_context():
            dict=r.table('backups').get(id).run(db.conn)            
            r.table('backups').get(id).update({'status':'Dumping to file'}).run(db.conn)
        with open(path+id+'.rethink', 'wb') as isard_rethink_file:
            pickle.dump(dict, isard_rethink_file)
        with open(path+id+'.json', 'wb') as isard_db_file:
            pickle.dump(isard_db, isard_db_file)
        with app.app_context():
            r.table('backups').get(id).update({'status':'Compressing'}).run(db.conn)
        with tarfile.open(path+id+'.tar.gz', "w:gz") as tar:
            tar.add(path+id+'.json', arcname=os.path.basename(path+id+'.json'))
            tar.add(path+id+'.rethink', arcname=os.path.basename(path+id+'.rethink'))
            tar.close()
        try:
            os.remove(path+id+'.json')
            os.remove(path+id+'.rethink')
        except OSError:
            pass
        with app.app_context():
            r.table('backups').get(id).update({'status':'Finished creating'}).run(db.conn)

    def recreate_table(self,tbl_data):
        if not r.table_list().contains(tbl_data['name']).run(db.conn):
            log.info("Restoring table {}".format(k))
            r.table_create(tbl_data['name'], primary_key=tbl_data['primary_key']).run(db.conn)
            for idx in tbl_data['indexes']:
                r.table(tbl_data['name']).index_create(idx).run(db.conn)
                r.table(tbl_data['name']).index_wait(idx).run(db.conn)
                log.info('Created index: {}'.format(idx))
                
    def restore_db(self,id):
        with app.app_context():
            dict=r.table('backups').get(id).run(db.conn)
            r.table('backups').get(id).update({'status':'Uncompressing backup'}).run(db.conn)
        path=dict['path']
        with tarfile.open(path+id+'.tar.gz', "r:gz") as tar:
            tar.extractall(path)
            tar.close()
        with app.app_context():
            r.table('backups').get(id).update({'status':'Loading data..'}).run(db.conn)
        with open(path+id+'.rethink', 'rb') as tbl_data_file:
            tbl_data = pickle.load(tbl_data_file)
        with open(path+id+'.json', 'rb') as isard_db_file:
            isard_db = pickle.load(isard_db_file)
        for k,v in isard_db.items():
            with app.app_context():
                try:
                    self.recreate_table(tbl_data[k])
                except Exception as e:
                    pass
                if not r.table_list().contains(k).run(db.conn):
                    log.error("Table {} not found, should have been created on IsardVDI startup.".format(k))
                    continue
                    #~ return False
                else:
                    log.info("Restoring table {}".format(k))
                    with app.app_context():
                        r.table('backups').get(id).update({'status':'Updating table: '+k}).run(db.conn)
                    # Avoid updating admin user!
                    if k == 'users': v[:] = [u for u in v if u.get('id') != 'admin']
                    log.info(r.table(k).insert(v, conflict='update').run(db.conn))
        with app.app_context():
            r.table('backups').get(id).update({'status':'Finished restoring'}).run(db.conn)
        try:
            os.remove(path+id+'.json')
            os.remove(path+id+'.rethink')
        except OSError as e:
            log.error(e)
            pass

    def download_backup(self,id):
        with app.app_context():
            dict=r.table('backups').get(id).run(db.conn)
        with open(dict['path']+dict['filename'], 'rb') as isard_db_file:
            return dict['path'],dict['filename'], isard_db_file.read()
            
    def info_backup_db(self,id):
        with app.app_context():
            dict=r.table('backups').get(id).run(db.conn)
            #~ r.table('backups').get(id).update({'status':'Uncompressing backup'}).run(db.conn)
        path=dict['path']
        with tarfile.open(path+id+'.tar.gz', "r:gz") as tar:
            tar.extractall(path)
            tar.close()
        #~ with app.app_context():
            #~ r.table('backups').get(id).update({'status':'Loading data..'}).run(db.conn)
        with open(path+id+'.rethink', 'rb') as tbl_data_file:
            tbl_data = pickle.load(tbl_data_file)
        with open(path+id+'.json', 'rb') as isard_db_file:
            isard_db = pickle.load(isard_db_file)
        i=0
        for sch in isard_db['scheduler_jobs']:
            isard_db['scheduler_jobs'][i].pop('job_state',None)
            i=i+1
        #~ i=0
        #~ for sch in isard_db['users']:
            #~ isard_db['users'][i].pop('password',None)
            #~ i=i+1            
        try:
            os.remove(path+id+'.json')
            os.remove(path+id+'.rethink')
        except OSError as e:
            log.error(e)
            pass
        return tbl_data,isard_db

    def check_new_values(self,table,new_data):
        backup=new_data
        dbb=list(r.table(table).run(db.conn))
        result=[]
        for b in backup:
            found=False
            for d in dbb:
                if d['id']==b['id']:
                    found=True
                    b['new_backup_data']=False
                    result.append(b)
                    break
            if not found: 
                b['new_backup_data']=True
                result.append(b)
        return result
    
    def upload_backup(self,handler):
        path='./backups/'
        id=handler.filename.split('.tar.gz')[0]
        filename = secure_filename(handler.filename)
        handler.save(os.path.join(path+filename))
        #~ with app.app_context():
            #~ dict=r.table('backups').get(id).run(db.conn)
            #~ r.table('backups').get(id).update({'status':'Uncompressing backup'}).run(db.conn)
        #~ path=dict['path']
        
        with tarfile.open(path+handler.filename, "r:gz") as tar:
            tar.extractall(path)
            tar.close()
        #~ with app.app_context():
            #~ r.table('backups').get(id).update({'status':'Loading data..'}).run(db.conn)
        with open(path+id+'.rethink', 'rb') as isard_rethink_file:
            isard_rethink = pickle.load(isard_rethink_file)
        with app.app_context():
            log.info(r.table('backups').insert(isard_rethink, conflict='update').run(db.conn))
        with app.app_context():
            r.table('backups').get(id).update({'status':'Finished uploading'}).run(db.conn)
        try:
            os.remove(path+id+'.json')
            os.remove(path+id+'.rethink')
        except OSError as e:
            log.error(e)
            pass
        
    def remove_backup_db(self,id):
        with app.app_context():
            dict=r.table('backups').get(id).run(db.conn)
        path=dict['path']
        try:
            os.remove(path+id+'.tar.gz')
        except OSError:
            pass
        with app.app_context():
            r.table('backups').get(id).delete().run(db.conn)
                    
    '''
    GRAPHS
    '''
    def get_domains_tree(self, id):
        #~ Should verify something???
        with app.app_context():
            rdomains=r.db('isard').table('domains')
            domains=r.table('domains').filter({'create_dict':{'origin':id}}).pluck('id','name').run(db.conn)
            dict={'name':id,'children':[]}
            for d in domains:
                children=r.table('domains').filter({'create_dict':{'origin':d['create_dict']['origin']}}).pluck('id','name').run(db.conn)
                dict['children'].append({'name':d['name'],'size':100})
            return dict

    def get_domains_tree_list(self):
        #~ Should verify something???
        with app.app_context():
            rdomains=r.db('isard').table('domains').pluck('id','name','kind',{'create_dict':{'origin'}}).run(db.conn)
            domains=[{'id':'isard','kind':'menu','name':'isard'},
                    {'id':'bases','kind':'menu','name':'bases','parent':'isard'},
                    {'id':'base_images','kind':'menu','name':'base_images','parent':'isard'}]
            for d in rdomains:
                try:
                    if not d['create_dict']['origin']:
                        if d['kind']=='base':
                            domains.append({'id':d['id'],'kind':d['kind'],'name':d['name'],'parent':'bases'})
                        else:
                            domains.append({'id':d['id'],'kind':d['kind'],'name':d['name'],'parent':'base_images'})
                    else:
                        domains.append({'id':d['id'],'kind':d['kind'],'name':d['name'],'parent':d['create_dict']['origin']})
                except Exception as e:
                    log.error('Exception on domain tree\n'+str(d)+'\n'+str(e))
            return domains
            
    def get_domains_tree_csv(self, id):
        #~ Should verify something???
        with app.app_context():
            rdomains=r.db('isard').table('domains')
            domains=r.table('domains').filter({'create_dict':{'origin':id}}).pluck('id','name').run(db.conn)
            csv='id,value\n'+id+',\n'
            #~ dict={'name':id,'children':[]}
            for d in domains:
                csv=csv+id+'.'+d['id']+',100\n'
                #~ dict['children'].append({'name':d['name'],'size':100})
            return csv

    def get_dashboard(self):
        with app.app_context():
            return {'users': r.db('isard').table('users').count().run(db.conn),
                    'desktops': r.db('isard').table('domains').get_all('desktop', index='kind').count().run(db.conn),
                    'started': r.db('isard').table('domains').get_all('Started', index='status').count().run(db.conn),
                    'templates': r.db('isard').table('domains').filter(r.row['kind'].match('template')).count().run(db.conn),
                    'isos': r.db('isard').table('isos').count().run(db.conn)}
    '''
    VIRT-BUILDER VIRT-INSTALL
    '''

    def domain_from_virtbuilder(self, user, name, description, icon, create_dict, hyper_pools, disk_size):
        with app.app_context():
            userObj=r.table('users').get(user).pluck('id','category','group').run(db.conn)
            create_dict['install']['options']='' #r.table('domains_virt_install').get(create_dict['install']['id']).pluck('options').run(db.conn)['options']
        
        parsed_name = app.isardapi.parse_string(name)
        dir_disk, disk_filename = app.isardapi.get_disk_path(userObj, parsed_name)
        create_dict['hardware']['disks']=[{'file':dir_disk+'/'+disk_filename,
                                            'size':disk_size}]   # 15G as a format
        new_domain={'id': '_'+user+'_'+parsed_name,
                  'name': name,
                  'description': description,
                  'kind': 'desktop',
                  'user': userObj['id'],
                  'status': 'CreatingFromBuilder',
                  'detail': None,
                  'category': userObj['category'],
                  'group': userObj['group'],
                  'xml': None,
                  'icon': icon,
                  'server': False,
                  'os': create_dict['builder']['id'],   #### Or name

                  'create_dict': create_dict, 
                  'hypervisors_pools': hyper_pools,
                  'allowed': {'roles': False,
                              'categories': False,
                              'groups': False,
                              'users': False}}
        with app.app_context():
            return self.check(r.table('domains').insert(new_domain).run(db.conn),'inserted')

    def domain_from_media(self, user, name, description, icon, create_dict, hyper_pools, disk_size):
        with app.app_context():
            userObj=r.table('users').get(user).pluck('id','category','group').run(db.conn)
        
        parsed_name = app.isardapi.parse_string(name)
        dir_disk, disk_filename = app.isardapi.get_disk_path(userObj, parsed_name)
        create_dict['hardware']['disks']=[{'file':dir_disk+'/'+disk_filename,
                                            'size':disk_size}]   # 15G as a format
        media=r.table('media').get(create_dict['media']).run(db.conn)
        if media['kind']=='iso':
            create_dict['hardware']['isos']=[{'id': create_dict['media']}]
            create_dict['hardware']['floppies']=[]     
        if media['kind']=='floppy':
            create_dict['hardware']['isos']=[]
            create_dict['hardware']['floppies']=[{'id': create_dict['media']}]                                                                                           
        new_domain={'id': '_'+user+'_'+parsed_name,
                  'name': name,
                  'description': description,
                  'kind': 'desktop',
                  'user': userObj['id'],
                  'status': 'CreatingDiskFromScratch',
                  'detail': None,
                  'category': userObj['category'],
                  'group': userObj['group'],
                  'xml': None,
                  'icon': icon,
                  'server': False,
                  'os': create_dict['create_from_virt_install_xml'],   #### Or name

                  'create_dict': create_dict, 
                  'hypervisors_pools': hyper_pools,
                  'allowed': {'roles': False,
                              'categories': False,
                              'groups': False,
                              'users': False}}
        with app.app_context():
            return self.check(r.table('domains').insert(new_domain).run(db.conn),'inserted')

    # ~ def isa_group_separator(self,line):
        # ~ return True if line.startswith('[') else False

    # ~ def update_virtbuilder(self,url="http://libguestfs.org/download/builder/index"):
        # ~ path=app.root_path+'/config/virt/virt-builder-files.ini'
        # ~ response = requests.get(url)
        # ~ file = open(path, "w")
        # ~ file.write(response.text)
        # ~ file.close()
        # ~ images=[]
        # ~ with open(path) as f:
            # ~ for key,group in itertools.groupby(f,self.isa_group_separator):
                # ~ if not key:
                    # ~ data={}
                    # ~ for item in group:
                        # ~ try:
                            # ~ if item.startswith(' '): continue
                            # ~ field,value=item.split('=')
                            # ~ value=value.strip()
                            # ~ data[field]=value
                        # ~ except Exception as e:
                            # ~ continue
                    # ~ data['id']=data['file'].split('.xz')[0]
                    # ~ if 'revision' not in data: data['revision']='0'
                    # ~ images.append(data)
        # ~ r.table('domains_virt_builder').insert(images, conflict='update').run(db.conn)
        # ~ return True

    # ~ def cmd_virtbuilder(self,id,path,size):
        # ~ command_output=subprocess.getoutput(['virt-builder '+id+' \
             # ~ --output '+path+' \
             # ~ --size '+size+'G \
             # ~ --format qcow2'])
        # ~ return True

    # ~ def update_virtinstall(self):
        # ~ data = subprocess.getoutput("osinfo-query os")
        # ~ installs=[]
        # ~ found=False
        # ~ for l in data.split('\n'):
            # ~ if not found:
                # ~ if '+' in l:
                    # ~ found=True
                # ~ continue
            # ~ else:
                # ~ v=l.split('|')
                # ~ installs.append({'id':v[0].strip(),'name':v[1].strip(),'vers':v[2].strip(),'www':v[3].strip()})
        # ~ r.table('domains_virt_install').insert(installs, conflict='update').run(db.conn)

    # ~ '''
    # ~ RESOURCES
    # ~ '''

    # ~ def get_remote_resources(self):
        # ~ with app.app_context():
            # ~ url=r.table('config').get('1').pluck('resources_url').run(db.conn)['url']
        # ~ path=app.root_path+'/config/virt/virt-builder-files.ini'
        # ~ response = requests.get(url)
        # ~ file = open(path, "w")
        # ~ file.write(response.text)
        # ~ file.close()
        # ~ images=[]
        # ~ with open(path) as f:
            # ~ for key,group in itertools.groupby(f,self.isa_group_separator):
                # ~ if not key:
                    # ~ data={}
                    # ~ for item in group:
                        # ~ try:
                            # ~ if item.startswith(' '): continue
                            # ~ field,value=item.split('=')
                            # ~ value=value.strip()
                            # ~ data[field]=value
                        # ~ except Exception as e:
                            # ~ continue
                    # ~ data['id']=data['file'].split('.xz')[0]
                    # ~ if 'revision' not in data: data['revision']='0'
                    # ~ images.append(data)
        # ~ r.table('domains_virt_builder').insert(images, conflict='update').run(db.conn)
        # ~ return True


    # ~ '''
    # ~ CLASSROOMS
    # ~ '''
    # ~ def replace_hosts_viewers_items(self,place,hosts):
        # ~ with app.app_context():
            # ~ try:
                # ~ place['id']=app.isardapi.parse_string(place['name'])
                # ~ r.table('places').insert(place, conflict='update').run(db.conn)
            # ~ except Exception as e:
                # ~ log.error('error on update place:',e)
                # ~ return False
                
            # ~ try:
                # ~ hosts = [dict(item, place_id=place['id']) for item in hosts]
                # ~ hosts = [dict(item, enabled=True) for item in hosts]
                # ~ r.table('hosts_viewers').get_all(place['id'], index='place_id').delete().run(db.conn)
                
                # ~ return self.check(r.table('hosts_viewers').insert(hosts).run(db.conn),'inserted')
            # ~ except Exception as e:
                # ~ log.error('error o update hosts_viewers:',e)
                # ~ return False


    # ~ def get_hosts_viewers(self, place_id):
        # ~ with app.app_context():
            # ~ return list(r.table('hosts_viewers').get_all(place_id, index='place_id').run(db.conn))
            


    '''
    ENGINE API
    '''
    def engine_action(self,action='info'):
        try:
            actions=['info','restart']
            if action not in actions: return False
            action='/engine_'+action
                
            with app.app_context():
                engine_api=r.table('config').get(1).run(db.conn)
            req=requests.post(engine_api['url']+':'+engine_api['web_port']+action, allow_redirects=False, verify=False, timeout=3)
            if req.status_code==200:
                return True
            else:
                log.error('Error response code: '+str(req.status_code)+'\nDetail: '+req.json())
        except Exception as e:
            log.error("Error contacting.\n"+str(e))
        return False
        
'''
FLATTEN AND UNFLATTEN DICTS
'''        
class flatten(object):
    def __init__(self):
        None

    def table_header_bstrap(self, table, pluck=None, editable=False):
        columns=[]
        for key, value in list(self.flatten_table_keys(table,pluck).items()):
            if editable and key is not 'id':
                columns.append({'field':key,'title':key, 'sortable': True, 'editable': True})
            else:
                columns.append({'field':key,'title':key})
        return columns
        
    def table_values_bstrap(self, rethink_cursor):
        data_in=list(rethink_cursor)
        data_out=[]
        for d in data_in:
            data_out.append(self.flatten_dict(d))
        return data_out
                   
    def flatten_table_keys(self,table,pluck=None):
        with app.app_context():
            if pluck is not None:
                d = r.table(table).pluck(pluck).nth(0).run(db.conn)
            else:
                d = r.table(table).nth(0).run(db.conn)
        def items():
            for key, value in list(d.items()):
                if isinstance(value, dict):
                    for subkey, subvalue in list(self.flatten_dict(value).items()):
                        yield key + "." + subkey, subvalue
                else:
                    yield key, value

        return dict(items())
        
    def flatten_dict(self,d):
        def items():
            for key, value in list(d.items()):
                if isinstance(value, dict):
                    for subkey, subvalue in list(self.flatten_dict(value).items()):
                        yield key + "-" + subkey, subvalue
                else:
                    yield key, value
        return dict(items())

    def unflatten_dict(self,dictionary):
        resultDict = dict()
        for key, value in dictionary.items():
            parts = key.split("-")
            d = resultDict
            for part in parts[:-1]:
                if part not in d:
                    d[part] = dict()
                d = d[part]
            d[parts[-1]] = value
        return resultDict

