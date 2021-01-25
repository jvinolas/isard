the basics
https://oswalt.dev/2013/10/introduction-to-open-vswitch/

ovs schema
https://www.google.com/url?sa=i&url=https%3A%2F%2Fmedium.com%2F%40fiberoptics%2Fopenvswitch-and-openflow-what-are-they-whats-their-relationship-d0ccd39b9a5c&psig=AOvVaw1vIoohGj_YCZK6zAfnYzW_&ust=1611564915233000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLikr6yZtO4CFQAAAAAdAAAAABAD

the master class
https://docs.openvswitch.org/en/latest/howto/userspace-tunneling/

cosicas
https://docs.openvswitch.org/en/latest/faq/issues/

ovs +wireguard
https://www.reddit.com/r/WireGuard/comments/hkablc/wireguard_with_openvswitch/
https://github.com/m13253/VxWireguard-Generator
https://gitlab.com/NickCao/RAIT

https://discuss.linuxcontainers.org/t/encrypted-vxlan-benefits-of-using-openvswitch-vs-native-driver/422/3

Conectar máquina virtual a vlan de la infrastructura
https://zcentric.com/2014/07/07/openvswitch-kvm-libvirt-ubuntu-vlans-the-right-way/

vxlan entre dos openvswitch
https://stackoverflow.com/questions/31566658/setup-private-networking-between-two-hosts-and-two-vms-with-libvirt-openvswitc

Simple conexió d'un guest a la xarxa del host via openvswitch
https://kashyapc.wordpress.com/2013/07/13/configuring-libvirt-guests-with-an-open-vswitch-bridge/

Configuració amb tunels GRE per a passar dues vlans
https://superuser.openstack.org/articles/multiple-private-networks-with-open-vswitch-gre-tunnels-and-libvirt/

Algo raro de libvirt pvlans
https://wiki.libvirt.org/page/OVS_and_PVLANS

Fet a mano, sense openvswitch
https://www.linux-kvm.org/page/Networking

No me mola però fa el que volem?
https://docs.openvswitch.org/en/latest/howto/vlan/

Ben explicat com conectar el ovswitch via nat o directe a eth0
https://literallymalwa.re/2019/05/openvswitch-configuration-for-libvirt-with-external-network-access/

Libvirt setting vlan
https://libvirt.org/formatnetwork.html#elementVlanTag

dnsmasq con ovs
https://topic.alibabacloud.com/a/integrates-open-vswitch-and-dnsmasq-to-provide-dhcp-functionality-for-virtual-machines_8_8_31422462.html

https://github.com/TrilliumIT/docker-vxlan-plugin

Plan B
https://icicimov.github.io/blog/docker/Container-networking/


Advanced que te cagas
https://docs.pica8.com/display/picos292cg/Configuring+VXLAN


http://networkstatic.net/configuring-vxlan-and-gre-tunnels-on-openvswitch/

Hay dos maneras de conectar las máquinas a una vlan:
a) Creando una network de libvirt que apunta al ovs con la vlan definida y añadiendo interfaz=network en libvirt
b) Indicando en el dominio la vlan
<interface type='bridge'>
<source bridge='ovsbr0'/>
<virtualport type='openvswitch'>
<parameters interfaceid='.....'/>
<virtualport>
<vlan>
<tag id='42'/>
</vlan>


########## hyper dockerfile

ovs-vsctl get Open_vSwitch . dpdk_initialized


## Add NET_ADMIN

apk add openvswitch
ovsdb-tool create /etc/openvswitch/conf.db
mkdir -pv /var/run/openvswitch/

# SCRIPT ON CONTAINER
ovsdb-server --detach --remote=punix:/var/run/openvswitch/db.sock --pidfile=ovsdb-server.pid --remote=ptcp:6640
ovs-vswitchd --detach --verbose --pidfile

ovs-vsctl add-br br-private


ovs-vsctl add-port br-private vx1 -- set interface vx1 type=vxlan options:remote_ip=172.31.1.102
ovs-vsctl add-port br-private vx1 -- set interface vx1 type=vxlan options:remote_ip=172.31.1.101


ovs-vsctl add-port br-private vx1 -- set interface vx1 type=vxlan options:remote_ip=176.9.99.248
ovs-vsctl add-port br-private vx1 -- set interface vx1 type=vxlan options:remote_ip=176.9.83.150

ovs-vsctl add-port br-private vxlan1 -- \
  set Interface vxlan1 type=vxlan options:remote_ip=172.31.1.102

<interface type='bridge'>
<source bridge='br-private'/>
<virtualport type='openvswitch'/>
<vlan>
<tag id='42'/>
</vlan>
</interface>

virsh attach-device 2 --file net.xml --current

Q: What destination UDP port does the VXLAN implementation in Open vSwitch use?

    A: By default, Open vSwitch will use the assigned IANA port for VXLAN, which is 4789. However, it is possible to configure the destination UDP port manually on a per-VXLAN tunnel basis. An example of this configuration is provided below.:

    $ ovs-vsctl add-br br0
    $ ovs-vsctl add-port br0 vxlan1 -- set interface vxlan1 type=vxlan \
        options:remote_ip=192.168.1.2 options:key=flow options:dst_port=8472


$ ovs-vsctl add-port br0 ipsec_gre0 -- \
            set interface ipsec_gre0 type=gre \
                               options:remote_ip=2.2.2.2 \
                               options:psk=swordfish
                               
You can use a self-signed certificate to do authentication. In each host, generate a certificate and the paired private key. Copy the certificate of the remote host to the local host and configure the OVS as following:

$ ovs-vsctl set Open_vSwitch . \
            other_config:certificate=/path/to/local_cert.pem \
            other_config:private_key=/path/to/priv_key.pem
$ ovs-vsctl add-port br0 ipsec_gre0 -- \
            set interface ipsec_gre0 type=gre \
                           options:remote_ip=2.2.2.2 \
                           options:remote_cert=/path/to/remote_cert.pem


####################

ovs-vsctl --may-exist add-br br-private \
  -- set Bridge br-private datapath_type=netdev \
  -- br-set-external-id br-private bridge-id br-private \
  -- set bridge br-private fail-mode=standalone
  
  
ovs-vsctl add-port br-private vm_port0 \
    -- set Interface vm_port0 type=dpdkvhostuser
  
ovs-vsctl add-port br-private vxlan0 \
  -- set interface vxlan0 type=vxlan options:remote_ip=172.168.1.2

ovs-vsctl --may-exist add-br br-phy \
    -- set Bridge br-phy datapath_type=netdev \
    -- br-set-external-id br-phy bridge-id br-phy \
    -- set bridge br-phy fail-mode=standalone \
         other_config:hwaddr=02:42:ac:14:00:05
         
         
ovs-vsctl add-br br-arun

