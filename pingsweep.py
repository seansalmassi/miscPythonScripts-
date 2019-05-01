#!/usr/bin/python

from scapy.all import *

TIMEOUT = 1
conf.verb = 0
for ip in range(1,256):
	packet = IP(dst="10.100.102." + str(ip), ttl=20)/ICMP()
	try:
	  reply = sr1(packet, timeout=TIMEOUT)
	  if not (reply is None):
		  print reply.dst, "is online"
	  else:
		  print "Time waiting for %s" % packet[IP].dst
  	except:
	  continue
