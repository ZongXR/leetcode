import numpy as np


class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        if all(np.array(nums) >= 0):
            return sum(nums)
        elif all(np.array(nums) <= 0):
            return max(nums)
        # result = [nums[0]]
        result_sum = nums[0]
        # current = [nums[0]]
        current_sum = nums[0]
        for x in nums[1:]:
            # new_current = deepcopy(current)
            # new_current.append(x)
            new_current_sum = current_sum + x
            if current_sum < new_current_sum:
                if x > new_current_sum:
                    temp = 0
                else:
                    temp = current_sum
                current_sum = x + temp
            else:
                current_sum = new_current_sum
            if current_sum > result_sum:
                # result = deepcopy(current)
                result_sum = current_sum
        return result_sum


if __name__ == "__main__":
    test = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # test = [-2, 1]
    # test = [-1, 0]
    # test = [2, 2, 0, -1]
    print(Solution().maxSubArray(test))
