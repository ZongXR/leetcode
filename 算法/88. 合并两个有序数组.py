"""
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。

 

示例 1：

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
示例 2：

输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        数组合并\n
        :param nums1: 第一个数组
        :param m: 第一个数组的长度
        :param nums2: 第二个数组
        :param n: 第二个数组的长度
        :return: 空
        """
        i = m - 1
        j = n - 1
        k = len(nums1) - 1
        while i >= 0 and j >= 0:
            x = nums1[i]
            y = nums2[j]
            if x > y:
                nums1[k] = x
                i = i - 1
            else:
                nums1[k] = y
                j = j - 1
            k = k - 1
        if i < 0:
            # 如果nums1先为空，此时nums2非空
            nums1[0:j + 1] = nums2[0:j + 1]


if __name__ == '__main__':
    # nums1 = [1, 2, 3, 0, 0, 0]
    # m = 3
    # nums2 = [2, 5, 6]
    # n = 3

    # nums1 = [2, 0]
    # m = 1
    # nums2 = [1]
    # n = 1

    # nums1 = [1]
    # m = 1
    # nums2 = []
    # n = 0

    # nums1 = [0, 0, 0, 0, 0]
    # m = 0
    # nums2 = [1, 2, 3, 4, 5]
    # n = 5

    nums1 = [4, 0, 0, 0, 0, 0]
    m = 1
    nums2 = [1, 2, 3, 5, 6]
    n = 5

    Solution().merge(nums1, m, nums2, n)
    print(nums1)
