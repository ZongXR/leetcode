from itertools import permutations


class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        return [list(x) for x in list(permutations(nums))]


if __name__ == "__main__":
    print(Solution().permute([1, 2, 3]))