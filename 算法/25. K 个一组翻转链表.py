# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


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
