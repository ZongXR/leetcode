# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


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
    