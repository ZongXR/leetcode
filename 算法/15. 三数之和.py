"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
示例 3：

输入：nums = [0]
输出：[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j = j + 1
                    k = k - 1
                    while j < k and nums[j] == nums[j-1]:
                        j = j + 1
                    while j < k and nums[k] == nums[k+1]:
                        k = k - 1
                    continue
                elif nums[i] + nums[j] + nums[k] > 0:
                    k = k - 1
                    continue
                elif nums[i] + nums[j] + nums[k] < 0:
                    j = j + 1
                    continue
        return result
