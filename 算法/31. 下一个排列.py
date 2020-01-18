class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums == sorted(nums, reverse=True):
            result = sorted(nums)
        elif nums[-2] < nums[-1]:
            result = nums.copy()
            result[-1], result[-2] = nums[-2], nums[-1]
        else:
            temp = nums[-1]
            for i in range(-2, -len(nums)-1, -1):
                if nums[i] >= temp:
                    temp = nums[i]
                    continue
                else:
                    # 记录下i，就是要交换的索引
                    # 记录下j，就是交换的索引
                    for j in range(-1, i, -1):
                        if nums[j] > nums[i]:
                            break
                    break
            result = nums.copy()
            result[i], result[j] = result[j], result[i]
            result = result[0:i+1] + sorted(result[i+1:])
        print(result)
        nums.clear()
        nums.extend(result)


if __name__ == "__main__":
    Solution().nextPermutation([1, 2, 6, 4, 3])
    Solution().nextPermutation([1, 5, 1])
    Solution().nextPermutation([2, 2, 7, 5, 4, 3, 2, 2, 1])