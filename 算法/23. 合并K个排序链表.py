# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

 

示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：

输入：lists = []
输出：[]
示例 3：

输入：lists = [[]]
输出：[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lst = []
        for link_list in lists:
            temp = []
            while link_list is not None:
                temp.append(link_list.val)
                link_list = link_list.next
            lst.extend(temp)
        lst.sort()
        if len(lst) == 0:
            return None
        elif len(lst) == 1:
            return ListNode(lst[0])
        else:
            new_lst = ListNode(lst[0])
            result = new_lst
        for x in lst[1:]:
            new_lst.next = ListNode(x)
            new_lst = new_lst.next
        return result
    