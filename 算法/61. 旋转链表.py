"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class ListNode:
    val: int

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        """
        遍历单链表\n
        :return: 字符串
        """
        node = self
        result = str(self.val) + " "
        while node is not None:
            node = node.next
            if node is not None:
                result = result + "-> %s " % str(node.val)
            else:
                result = result + "-> NULL"
        return result


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        旋转链表\n
        :param head: 链表的头
        :param k: 旋转刻度
        :return: 旋转后链表的头
        """
        if head is None:
            return None
        length = self.get_length(head)
        k = k % length
        step = length - k
        result = head
        node = head
        temp = None
        for i in range(0, length):
            if i == step - 1:
                temp = node
            if i == step:
                result = node
            if i == length - 1:
                node.next = head
            node = node.next
        temp.next = None
        return result

    def get_length(self, head: ListNode) -> int:
        """
        获取单链表的长度\n
        :param head: 链表的头
        :return: 链表的长度
        """
        node = head
        result = 0
        while True:
            if node is None:
                return result
            result = result + 1
            node = node.next


if __name__ == '__main__':
    root = ListNode(0, ListNode(1, ListNode(2, None)))
    print(Solution().rotateRight(root, 4))
