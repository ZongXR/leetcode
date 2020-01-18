class Solution:
    def firstMissingPositive(self, nums: [int]) -> int:
        if len(nums) == 0 or max(nums) <= 0:
            return 1
        for i in range(1, max(nums)+1):
            if i not in nums:
                return i
        return max(nums) + 1


if __name__ == "__main__":
    print(Solution().firstMissingPositive([7, 8, 9, 11, 12]))
    print(Solution().firstMissingPositive([1, 2, 0]))
    print(Solution().firstMissingPositive([]))