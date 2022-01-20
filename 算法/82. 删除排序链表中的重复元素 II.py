# -*- coding: utf-8 -*-
"""
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。
返回同样按升序排列的结果链表。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        result = head
        duplicate_node = None
        prev_node = None
        duplicate_value = None
        while head is not None:
            if head.val == duplicate_value:
                # 当前节点和上个节点重复，分为两种情况，重复序列的第二个节点、重复序列的之后的节点
                if prev_node is None or head.val == prev_node.val:
                    # 重复序列的第二个
                    if duplicate_node is not None:
                        duplicate_node.next = head.next
                    else:
                        result = head.next
                    head = head.next
                    prev_node = duplicate_node
                else:
                    prev_node.next = head.next
                    duplicate_value = head.val
                    head = head.next
            else:
                # 当前节点和上个节点不重复
                duplicate_node = prev_node
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