#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-03-26 23:30:57
# @Author  : libin (643599680@qq.com)
# @Version : v1.0

"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows. 
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            resultstr = str(x)[::-1]
        else:
            resultstr = str(x)[0] + str(x)[1:][::-1]
        resultInt = int(resultstr)
        if resultInt < -2**31 or resultInt > 2**31 - 1:
            resultInt = 0
        return resultInt


test = Solution()
print(test.reverse(1563847412))
