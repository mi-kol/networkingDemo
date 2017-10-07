#!/usr/bin/python

import socket

s = socket.socket()
port = 12345

s.connect(('10.0.0.68', port))
print(bytes.decode(s.recv(1024)))
s.close()