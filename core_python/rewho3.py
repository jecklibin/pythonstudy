#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-04-01 23:51:34
# @Author  : libin (643599680@qq.com)
# @Version : v1.0

import os
import re

with os.popen('who', 'r') as f:
    for eachline in f:
        print(re.split(r'\s\s+|\t', eachline.strip()))
