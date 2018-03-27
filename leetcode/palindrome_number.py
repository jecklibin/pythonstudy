#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-03-27 22:43:22
# @Author  : libin (643599680@qq.com)
# @Version : v1.0

"""
Determine whether an integer is a palindrome. Do this without extra space.
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]
