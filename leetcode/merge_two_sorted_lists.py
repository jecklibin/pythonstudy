#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-03-29 23:17:43
# @Author  : libin (643599680@qq.com)
# @Version : v1.0

"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        nodeHead = ListNode(0)
        nodeTail = nodeHead
        while(l1 and l2):
            if l1.val <= l2.val:
                newNode = ListNode(l1.val)
                l1 = l1.next
            else:
                newNode = ListNode(l2.val)
                l2 = l2.next
            nodeTail.next = newNode
            nodeTail = newNode

        while(l1):
            newNode = ListNode(l1.val)
            nodeTail.next = newNode
            nodeTail = newNode
            l1 = l1.next

        while(l2):
            newNode = ListNode(l2.val)
            nodeTail.next = newNode
            nodeTail = newNode
            l2 = l2.next
        return nodeHead.next
