class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        i = 0
        while len(nums) >= 2:
            x = nums.pop(0)
            if target - x in nums:
                return [i, i + nums.index(target - x) + 1]
            else:
                i = i + 1
