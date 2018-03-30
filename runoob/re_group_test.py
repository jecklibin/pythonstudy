#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-03-30 21:40:44
# @Author  : libin (643599680@qq.com)
# @Version : v1.0

import re

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) :", matchObj.group(2))
else:
    print("No match!!")
