cd /certs
if [ ! -f /certs/server_private.key ]
then
    ## Alert! All client public keys should be updated in databas
    ## It is done afterwards in wgadmin
    wg genkey | tee server_private.key | wg pubkey > server_public.key
fi

# Allows wireguard to reach guests in hypervisor
#ip r a $WG_HYPER_GUESTNET via $WG_HYPER_NET_HYPER_PEER
cd /src
sleep infinity
#python3 wgadmin.py
