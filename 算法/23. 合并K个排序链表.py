# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


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
    