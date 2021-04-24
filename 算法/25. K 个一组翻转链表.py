# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

进阶：

你可以设计一个只使用常数额外空间的算法来解决此问题吗？
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
 

示例 1：


输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]
示例 2：


输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]
示例 3：

输入：head = [1,2,3,4,5], k = 1
输出：[1,2,3,4,5]
示例 4：

输入：head = [1], k = 1
输出：[1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        stack = []
        if head is None:
            return None
        elif head.next is None:
            return head
        new_lst = ListNode(None)
        result = new_lst
        while head is not None:
            while len(stack) < k:
                flag = True
                if head is None:
                    flag = False
                    break
                stack.append(head.val)
                head = head.next
            while len(stack) > 0:
                if flag:
                    new_lst.next = ListNode(stack.pop())
                    new_lst = new_lst.next
                else:
                    new_lst.next = ListNode(stack.pop(0))
                    new_lst = new_lst.next
        while len(stack) > 0:
            new_lst.next = ListNode(stack.pop())
            new_lst = new_lst.next
        return result.next
