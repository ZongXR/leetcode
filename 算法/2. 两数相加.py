"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

 

示例 1：


输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        new_num = 0
        test = result
        flag1 = True
        flag2 = True
        while True:
            try:
                num1 = l1.val
                l1 = l1.next
            except AttributeError:
                num1 = 0
                flag1 = False
            try:
                num2 = l2.val
                l2 = l2.next
            except AttributeError:
                num2 = 0
                flag2 = False
            if (flag1 is False) and (flag2 is False) and (new_num == 0):
                break
            else:
                result.val = (num1 + num2 + new_num) % 10
                new_num = (num1 + num2 + new_num) // 10
                if new_num > 0 or (l1 is not None) or (l2 is not None):
                    result.next = ListNode(0)
                    result = result.next
        return test

