#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-03-28 23:36:24
# @Author  : libin (643599680@qq.com)
# @Version : v1.0

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        brackets = {'(': ')', '{': '}', '[': ']'}
        leftchrs = brackets.keys()
        rightchrs = brackets.values()
        for element in s:
            if element in leftchrs:
                stack.append(element)
            elif element in rightchrs:
                if not stack:
                    return False
                leftchr = stack.pop()
                if brackets[leftchr] != element:
                    return False
        if stack:
            return False
        else:
            return True
