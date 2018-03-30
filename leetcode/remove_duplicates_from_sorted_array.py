#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-03-30 23:15:24
# @Author  : libin (643599680@qq.com)
# @Version : v1.0

"""
 Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        before = nums[0] - 1
        index = 0
        for value in nums:
            if value == before:
                continue
            else:
                nums[index] = value
                index += 1
                before = value
        del nums[index:]
        return index


if __name__ == "__main__":
    l = [1, 1, 2, 3, 3]
    test = Solution()
    print(test.removeDuplicates(l))
    print(l)
