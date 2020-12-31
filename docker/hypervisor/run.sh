rm -rf /run/libvirt/*
echo "Generating selfsigned certs for spice client..."
sh auto-generate-certs.sh

echo "Setting wireguard.xml network for $WG_HYPER_GUESTNET"
bash wireguard.sh
ip r a $WG_CLIENTS_NET via ${WG_HYPER_NET_WG_PEER}

echo "Starting libvirt daemon..."
chown root:kvm /dev/kvm
/usr/sbin/virtlogd &
sleep 2
/usr/sbin/libvirtd &
sleep 1
#/usr/bin/virsh net-start default
sh -c "/vlans-discover.sh"

FILES=/etc/libvirt/qemu/networks/*
for f in $FILES
do
  filename=$(basename -- "$f")
  filename="${filename%.*}"
  if [ $filename != "autostart" ]; then
    echo "Activating network: $filename"
    /usr/bin/virsh net-start $filename
    /usr/bin/virsh net-autostart $filename
  fi
done


echo "Checking hypervisor..."
echo "[1/1] basic domain start..."
virsh create checks/domain.xml
virsh destroy domain
ssh-keygen -A -f /usr/local/
/usr/sbin/sshd -D -e -f /etc/ssh/sshd_config
