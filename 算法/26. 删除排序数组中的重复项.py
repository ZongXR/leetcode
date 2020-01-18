class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        temp = sorted(list(set(nums)))
        nums.clear()
        nums.extend(temp)
        return len(nums)