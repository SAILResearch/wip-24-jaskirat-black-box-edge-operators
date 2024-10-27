tc qdisc del dev eth0 root
tc qdisc del dev eth0 ingress
tc qdisc add dev eth0 ingress
tc filter add dev eth0 parent ffff: protocol ip u32 match ip src 0.0.0.0/0 police rate 200mbit burst 200mbit mtu 200mbit drop flowid :1
tc qdisc add dev eth0 root tbf rate 200mbit burst 200mbit limit 200mbit mtu 200mbit
