#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-03-27 23:04:46
# @Author  : libin (643599680@qq.com)
# @Version : v1.0

"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        relation = {'I': 1, 'V': 5, 'X': 10,
                    'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        record = 0
        for iter in s:
            value = relation[iter]
            if value <= record:
                result = result + record
                record = value
            else:
                result = result - record
                record = value
        result = result + record
        return result
