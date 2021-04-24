# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

进阶：你能尝试使用一趟扫描实现吗？

 

示例 1：


输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：

输入：head = [1], n = 1
输出：[]
示例 3：

输入：head = [1,2], n = 1
输出：[1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def removeNthFromEnd(self, head, n: int):
        # 记录开头
        header = head
        length = 0
        while head.next is not None:
            length = length + 1
            head = head.next
        if n == length+1:
            return header.next
        result = header
        for i in range(length-n):
            header = header.next
        temp = header.next
        try:
            header.next = temp.next
            return result
        except Exception as e:
            print(type(e), e)
            return None
