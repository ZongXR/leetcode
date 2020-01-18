class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return sorted(nums + [target]).index(target)