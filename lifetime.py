#!/usr/bin/env python3
from scapy.all import Ether,ICMP,IP,TCP,srp1,sniff,sendp
import os
'''
Normal_Group/Normal_1/Normal-h3_1.pcap
Normal_Group/Normal_2/Normal-h3_2.pcap
...
Normal_Group/Normal_6/Normal-h3_6.pcap
Normal_Group/Normal_7/Normal-h3_8.pcap
Normal_Group/Normal_8/Normal-h3_9.pcap
...
Normal_Group/Normal_11/Normal-h3_12.pcap
'''
#traffic=sniff(offline="/home/user/Desktop/reflector/Normal_Group/Normal_1/Normal-h3_1.pcap",filter="ip dst host 192.168.20.133")
'''
for pkt in traffic:
	pkt.getlayer(IP).src='10.0.0.2'
	pkt.getlayer(IP).dst='10.0.0.1'
	pkt.src='00:00:0a:00:00:02'
	pkt.dst='00:00:0a:00:00:01'
'''
#sendp(traffic[0:10],iface='A-eth0')
#os.system('./ufonet/ufonet -a 10.0.0.1 -t 10.0.0.4 --tachyon=TACHYON 101')
#os.system('./ufonet/ufonet -a "10.0.0.1" -t 10.0.0.4 --tachyon "TACHYON 101"')
