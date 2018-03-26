#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-03-26 22:52:13
# @Author  : libin (643599680@qq.com)
# @Version : v1.0

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.


Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1 = 0
        for value1 in nums:
            value2 = target - value1
            if value2 in nums:
                index2 = nums.index(value2)
                if index1 == index2:
                    index1 = index1 + 1
                    continue
                else:
                    break
            index1 = index1 + 1
        return [index1, index2]


test = Solution()
print(test.twoSum([2, 7, 11, 17], 9))
