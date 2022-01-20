# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        result = head
        prev_node = None
        duplicate_value = None
        while head is not None:
            if head.val == duplicate_value:
                prev_node.next = head.next
                duplicate_value = head.val
                head = head.next
            else:
                # 当前节点和上个节点不重复
                prev_node = head
                duplicate_value = head.val
                head = head.next
        return result


if __name__ == '__main__':
    node8 = ListNode(5, None)
    node7 = ListNode(5, node8)
    node6 = ListNode(4, node7)
    node5 = ListNode(4, node6)
    node4 = ListNode(2, node5)
    node3 = ListNode(1, node4)
    node2 = ListNode(1, node3)
    node1 = ListNode(1, node2)
    kk = Solution().deleteDuplicates(node1)
    while kk is not None:
        print(kk.val, end=" ")
        kk = kk.next