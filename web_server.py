#!/usr/bin/python3
# Shyam Govardhan
# 25 December 2018
# Coursera: Interfacing with the Raspberry Pi
# Week 2 Assignment

import socket
import sys
import os

SERVER_HOST = "192.168.0.29" # RaspberryPi's IP address; for accessing over the network
SERVER_PORT = 80             # Web server port
REQUEST_BACKLOG = 5
HTTP_ACK = "Got a request!"  # ACK sent by the web server to the client browser

requestCount = 1             # tally of number of requests processed

# The web server keeps a count of number of requests it receives and this 
# number is deplayed to the user, along with the ACK "Got a request!"
def getHtmlResponse():
    htmlAck= "<h2 style=\"color:Tomato;\">%s</h2><h3 style=\"color:DodgerBlue;\">Request Count: %d</h3>" % (HTTP_ACK, requestCount / 2)
    htmlBody = "<html><body>%s</body></html>" % htmlAck 
    #htmlBody = "<html><body>%s</body></html>" % getHtmlAck()
    httpHeader = "HTTP/1.0 200 OK\r\nContent-Length: %d\r\nContent-Type: text/html; charset=UTF-8" % len(htmlBody)
    htmlResponse = httpHeader + "\r\n\r\n" + htmlBody + "\r\n"
    return htmlResponse

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.bind((SERVER_HOST, SERVER_PORT))
    mysock.listen(REQUEST_BACKLOG)
    while True:
        conn, addr = mysock.accept()
        data = conn.recv(1000)
        if not data:
            break   
        requestCount += 1
        print("requestCount: %d" % requestCount)
        htmlResponse = getHtmlResponse()
        conn.sendall(bytes(htmlResponse, encoding='ascii'))
    conn.close()
    mysock.close()
except OSError as e:
    print("Failed to load: errno(%d); strerror(%s)" % (e.errno, e.strerror))
    sys.exit()
except KeyboardInterrupt:  
    print("Interrupted by user (^C)... Cleaning up...") 
    sys.exit()
