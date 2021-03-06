#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-04-12 00:08:10
# @Author  : libin (643599680@qq.com)
# @Version : v1.0

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    udpCliSock.sendto(bytes(data, 'utf-8'), ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))
udpCliSock.close()
