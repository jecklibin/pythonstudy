#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-04-01 01:10:41
# @Author  : libin (643599680@qq.com)
# @Version : v1.0

"""
 Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
