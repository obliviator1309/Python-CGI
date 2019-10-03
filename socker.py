#!/usr/bin/python36
 
import socket
import sys

try: 
	s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
	print ("Socket successfully created")

except socket.error as err:
	print ("socket failed")

port = 1234

try: 
	host_ip = socket.gethostbyname ('192.168.43.206')
except socket.gaierror:
	print ("there was error resolving in host")
	sys.exit()

s.connect (('192.168.43.206' , 1234))
#print ("the socket has success on port")
print ("the socket has success on port == %s" %'192.168.43.206')
