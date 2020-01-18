from itertools import permutations


class Solution:
    def permuteUnique(self, nums: [int]) -> [[int]]:
        temp = [list(x) for x in permutations(nums)]
        result = []
        [result.append(x) for x in temp if x not in result]
        return result


if __name__ == "__main__":
    print(Solution().permuteUnique([1, 1, 2]))