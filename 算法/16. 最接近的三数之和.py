"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

 

示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
        nums.sort()
        result_new = [nums[0], nums[1], nums[-1]]
        dist = abs(target) + sum(map(abs, nums))
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                result = [nums[i], nums[j], nums[k]]
                new_dist = target - sum(result)
                if new_dist == 0:
                    return target
                elif new_dist > 0:
                    if abs(new_dist) < abs(dist):
                        result_new = [nums[i], nums[j], nums[k]]
                        dist = new_dist
                    j = j + 1
                    while j < k and nums[j] == nums[j-1]:
                        j = j + 1
                    continue
                elif new_dist < 0:
                    if abs(new_dist) < abs(dist):
                        result_new = [nums[i], nums[j], nums[k]]
                        dist = new_dist
                    k = k - 1
                    while j < k and nums[k] == nums[k+1]:
                        k = k - 1
                    continue
        return sum(result_new)


if __name__ == "__main__":
    nums = [1, 1, -1, -1, 3]
    target = -1
    print(Solution().threeSumClosest(nums, target))