#!/bin/sh
#$1 - add 
#$2 - 52:54:00:2c:7a:13 
#$3 - 192.168.128.76 
#$4 - slax

# Example env
#SHLVL=1 DNSMASQ_TIME_REMAINING=3600 DNSMASQ_REQUESTED_OPTIONS=1,28,2,3,15,6,119,12,44,47,26,121,42 DNSMASQ_LEASE_EXPIRES=1609700452 VIR_BRIDGE_NAME=virbr20 DNSMASQ_SUPPLIED_HOSTNAME=slax DNSMASQ_TAGS=virbr20 PWD=/ DNSMASQ_INTERFACE=virbr20

export VIR_BRIDGE_NAME=$VIR_BRIDGE_NAME
/usr/lib/libvirt/libvirt_leaseshelper $1 $2 $3 $4

source /tmp/env
export STATS_RETHINKDB_HOST=$STATS_RETHINKDB_HOST
export WEBAPP_ADMIN_PWD=$WEBAPP_ADMIN_PWD
/usr/bin/python3 /update-client-ips.py "$@"
