#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-04-11 23:26:04
# @Author  : libin (643599680@qq.com)
# @Version : v1.0

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send(bytes('[%s] %s' %
                              (ctime(), data.decode('utf-8')), 'utf-8'))
    tcpCliSock.close()
tcpSerSock.close()
