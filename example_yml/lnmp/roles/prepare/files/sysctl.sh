#!/bin/bash
grep "#Add Kernel Options" /etc/sysctl.conf
if [ $? -eq 1 ];then
cat>> /etc/sysctl.conf <<'EOF'
net.ipv4.tcp_max_syn_backlog = 65536
net.core.netdev_max_backlog =  32768
net.core.somaxconn = 32768
net.ipv4.tcp_synack_retries = 2
net.ipv4.tcp_syn_retries = 2
net.ipv4.tcp_tw_recycle = 1
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_max_orphans = 65536
net.ipv4.ip_local_port_range = 1024  65535
net.ipv4.tcp_keepalive_time = 30
EOF
else
echo "Kernel Options Adding completed"
fi
