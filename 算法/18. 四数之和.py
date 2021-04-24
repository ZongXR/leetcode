"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：答案中不可以包含重复的四元组。

 

示例 1：

输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
示例 2：

输入：nums = [], target = 0
输出：[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            # 如果判断过则跳过
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            for j in range(len(nums)-1, 2, -1):
                # 如果判断过则跳过
                if j <= len(nums) - 2 and nums[j] == nums[j+1]:
                    continue
                l = i + 1
                r = j - 1
                if l+1 < j and nums[i] + nums[l] + nums[l+1] + nums[j] > target:
                    continue
                elif i < r+1 and nums[i] + nums[r-1] + nums[r] + nums[j] < target:
                    continue
                while l < r:
                    arr = [nums[i], nums[l], nums[r], nums[j]]
                    if sum(arr) == target and arr not in result:
                        result.append(arr)
                        l = l + 1
                        r = r - 1
                        while l < r and nums[l] == nums[l-1]:
                            l = l + 1
                        while l < r and nums[r] == nums[r+1]:
                            r = r - 1
                        continue
                    elif sum(arr) < target:
                        l = l + 1
                        while l < r and nums[l] == nums[l-1]:
                            l = l + 1
                        continue
                    elif sum(arr) > target:
                        r = r - 1
                        while l < r and nums[r] == nums[r+1]:
                            r = r - 1
                        continue
        return result


if __name__ == "__main__":
    # print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
    # print(Solution().fourSum([5, 5, 3, 5, 1, -5, 1, -2], 4))
    print(Solution().fourSum([1, -2, -5, -4, -3, 3, 3, 5], -11))