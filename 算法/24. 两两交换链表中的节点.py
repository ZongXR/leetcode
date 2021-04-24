# Definition for singly-linked list.
"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例 1：


输入：head = [1,2,3,4]
输出：[2,1,4,3]
示例 2：

输入：head = []
输出：[]
示例 3：

输入：head = [1]
输出：[1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        lst = []
        while head is not None:
            lst.append(head.val)
            head = head.next
        if len(lst) == 0:
            return None
        elif len(lst) == 1:
            return ListNode(lst[0])
        stack = []
        new_lst = ListNode(lst[0])
        result = new_lst
        i = 0
        for x in lst:
            # 索引值等于0, 2, 4, 6, ...
            if i % 2 == 0:
                stack.append(x)
            # 索引值等于1, 3, 5, ...
            elif i % 2 != 0:
                new_lst.next = ListNode(x)
                new_lst = new_lst.next
                new_lst.next = ListNode(stack.pop())
                new_lst = new_lst.next
            i = i + 1
        if len(stack) > 0:
            new_lst.next = ListNode(stack.pop())
        result = result.next
        return result

