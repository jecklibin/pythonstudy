#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-04-02 00:12:51
# @Author  : libin (643599680@qq.com)
# @Version : v1.0

from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime

tlds = ('com', 'edu', 'net', 'org', 'gov')

for i in range(randrange(5, 11)):
    dtint = randrange(2**31 - 1)  # pick date
    dtstr = ctime(dtint)  # data string
    llen = randrange(4, 8)  # login is shorter
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)  # domain is longer
    dom = ''.join(choice(lc) for j in range(dlen))
    print('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login,
                                      dom, choice(tlds), dtint, llen, dlen))
