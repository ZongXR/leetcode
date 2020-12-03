"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import numpy as np
from copy import deepcopy


class Solution:
    def canJump(self, nums: [int]) -> bool:
        """
        贪婪算法\n
        :param nums: 数组
        :return: 是否能到达终点
        """
        while len(nums) > 0:
            max_range = self.get_max_range(nums)
            if len(max_range) == len(nums):
                return True
            if len(max_range) == 0:
                return False
            index = self.get_max_step(max_range)
            nums = nums[index:]
        return True

    def get_max_step(self, nums: [int]) -> int:
        """
        获得剩余最强跳跃能力的点的索引\n
        :param nums: 上一个点的可达区间
        :return: 剩余跳跃能力最强的点的索引
        """
        results = []
        for i, value in enumerate(nums):
            result = value - (len(nums) - i - 1)
            results.append(result)
        return np.argmax(results)

    def get_max_range(self, nums: [int]) -> [int]:
        """
        给一个点，返回最大跳跃范围\n
        :param nums: 序列
        :return: 跳跃范围
        """
        x = nums.pop(0)
        if x == 0:
            return []
        if x > len(nums):
            return deepcopy(nums)
        else:
            return deepcopy(nums[:x])


if __name__ == "__main__":
    print(Solution().canJump([3, 2, 1, 0, 4]))


