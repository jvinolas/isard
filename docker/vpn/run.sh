cd /certs
if [ ! -f /certs/server_private.key ]
then
    ## Alert! All client public keys should be updated in databas
    ## It is done afterwards in wgadmin
    wg genkey | tee server_private.key | wg pubkey > server_public.key
fi

# Allows wireguard to reach guests in hypervisors
#ip r a $WG_HYPER_GUESTNET via $WG_HYPER_NET_HYPER_PEER
ip r a 192.168.128.0/23 via 192.168.119.3
ip r a 192.168.130.0/23 via 192.168.119.5
ip r a 192.168.132.0/23 via 192.168.119.7
ip r a 192.168.134.0/23 via 192.168.119.9
ip r a 192.168.136.0/23 via 192.168.119.11
ip r a 192.168.138.0/23 via 192.168.119.13
ip r a 192.168.140.0/23 via 192.168.119.15
ip r a 192.168.142.0/23 via 192.168.119.17
ip r a 192.168.144.0/23 via 192.168.119.19

cd /src
python3 wgadmin.py
