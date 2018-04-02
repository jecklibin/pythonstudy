#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-04-03 00:28:08
# @Author  : libin (643599680@qq.com)
# @Version : v1.0

"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"

Example 2:

Input: 4
Output: "1211"
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        import itertools
        result = "1"
        count = 1
        while count < n:
            result = "".join(
                [str(len(list(g))) + k for k, g in itertools.groupby(result)])
            count += 1
        return result


if __name__ == "__main__":
    test = Solution()
    print(test.countAndSay(4))
    print(test.countAndSay(5))
