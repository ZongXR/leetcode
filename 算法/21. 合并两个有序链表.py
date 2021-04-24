# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

示例 1：


输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：

输入：l1 = [], l2 = []
输出：[]
示例 3：

输入：l1 = [], l2 = [0]
输出：[0]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is not None:
            return l2
        elif l1 is not None and l2 is None:
            return l1
        elif l1 is None and l2 is None:
            return None
        if l1.val < l2.val:
            new_lst = ListNode(l1.val)
            l1 = l1.next
        else:
            new_lst = ListNode(l2.val)
            l2 = l2.next
        result = new_lst
        while True:
            if l1 is None:
                temp = l2
                break
            elif l2 is None:
                temp = l1
                break
            if l1.val < l2.val:
                new_lst.next = ListNode(l1.val)
                l1 = l1.next
            else:
                new_lst.next = ListNode(l2.val)
                l2 = l2.next
            new_lst = new_lst.next
        new_lst.next = temp
        return result
    