#!/usr/bin/python

import socket

s = socket.socket()
port = 12345
s.bind(('', port))
print "Now listening."

s.listen(5)
while True:
    c, addr = s.accept()
    print("Got connection from", addr)
    c.send("Thank you for connecting")
    c.close()
