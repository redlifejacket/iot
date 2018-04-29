#!/usr/bin/python3
# Shyam Govardhan
# 29 April 2018

import socket
import sys

DATASIZE = 80
PORT = 80

DOMAIN = "cnn.com"
PAGE = "/2018/04/28/asia/modi-xi-summit-statement/index.html"

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Failed to create socket")
    sys.exit()
try:
    host = socket.gethostbyname(DOMAIN)
except socket.gaierror:
    print("Failed to get host")
    sys.exit()
mysock.connect((host, PORT))

message = ('GET %s HTTP/1.1\r\nHost: %s\r\n\r\n' % (PAGE, DOMAIN))

try:
    mysock.send(message.encode())
except socket.error:
    print("Failed to send")
    sys.exit()
data = mysock.recv(DATASIZE)
decodedString = data.decode()
print(decodedString[:DATASIZE])
