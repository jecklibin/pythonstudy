#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-03-30 23:33:20
# @Author  : libin (643599680@qq.com)
# @Version : v1.0

"""
Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        for value in nums:
            if value != val:
                nums[index] = value
                index += 1
        del nums[index:]
        return index


if __name__ == "__main__":
    test = Solution()
    l = [3, 2, 2, 3]
    print(test.removeElement(l, 3))
    print(l)
