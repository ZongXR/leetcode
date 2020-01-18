class Solution:
    def search(self, nums: [int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1

