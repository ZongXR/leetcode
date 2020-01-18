class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        try:
            left = nums.index(target)
            right = nums[::-1].index(target)
            return [left, len(nums) - right - 1]
        except ValueError:
            return [-1, -1]