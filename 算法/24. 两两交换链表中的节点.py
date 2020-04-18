# Definition for singly-linked list.
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

