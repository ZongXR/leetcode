# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from copy import deepcopy


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
