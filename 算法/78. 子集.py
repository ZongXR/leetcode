"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

 

示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from itertools import combinations


class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        """
        子集\n
        :param nums: 列表
        :return: 有哪些子集
        """
        if len(nums) == 0:
            return [[]]
        else:
            k = len(nums)
            result = [[]]
            for i in range(1, k + 1):
                result.extend(list(map(list, combinations(nums, i))))
            return result


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
    print(Solution().subsets([0]))
