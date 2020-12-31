# Allows hyper to reach wireguard clients
IFS=. read ip1 ip2 ip3 ip4 <<< "$WG_HYPER_GUESTNET"
GW=$ip1.$ip2.$ip3.1
IFS=/ read ip4 PREFIX <<< "$ip4"
cat > /etc/libvirt/qemu/networks/wireguard.xml << EOF
<network xmlns:dnsmasq='http://libvirt.org/schemas/network/dnsmasq/1.0'>
  <name>wireguard</name>
  <uuid>98552eb2-3e01-4f4d-9d50-4b824f31caff</uuid>
  <bridge name="virbr20"/>
  <forward mode="route" dev="eth1"/>
  <port isolated='yes'/>
  <ip address="$GW" prefix="$PREFIX">
    <dhcp>
      <range start="$WG_HYPER_GUESTNET_DHCP_START" end="$WG_HYPER_GUESTNET_DHCP_END"/>
    </dhcp>
  </ip>
       <dnsmasq:options>
        <dnsmasq:option value="dhcp-option=121,$WG_CLIENTS_NET,$GW"/>
      </dnsmasq:options>
</network>
EOF