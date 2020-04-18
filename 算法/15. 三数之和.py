class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j = j + 1
                    k = k - 1
                    while j < k and nums[j] == nums[j-1]:
                        j = j + 1
                    while j < k and nums[k] == nums[k+1]:
                        k = k - 1
                    continue
                elif nums[i] + nums[j] + nums[k] > 0:
                    k = k - 1
                    continue
                elif nums[i] + nums[j] + nums[k] < 0:
                    j = j + 1
                    continue
        return result
