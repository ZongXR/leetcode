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

