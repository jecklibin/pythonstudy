#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-03-28 23:03:04
# @Author  : libin (643599680@qq.com)
# @Version : v1.0

"""
Write a function to find the longest common prefix string amongst an array of strings. 
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        index = 0
        for index in range(len(strs[0])):
            for str in strs:
                if len(str) <= index or str[index] != strs[0][index]:
                    if index == 0:
                        return ""
                    else:
                        return strs[0][:index]
        return strs[0]
