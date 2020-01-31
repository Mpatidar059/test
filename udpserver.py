# -*- coding: utf-8 -*-

# Script to run UDP Server on 127.0.0.1:8126
# This mocks statsd server for testing

import socket

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 8126

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

while True:
    data, addr = serverSock.recvfrom(1024)
    print "Message===>: ", data
