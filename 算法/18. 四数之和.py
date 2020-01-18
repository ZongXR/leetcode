class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            # 如果判断过则跳过
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            for j in range(len(nums)-1, 2, -1):
                # 如果判断过则跳过
                if j <= len(nums) - 2 and nums[j] == nums[j+1]:
                    continue
                l = i + 1
                r = j - 1
                if l+1 < j and nums[i] + nums[l] + nums[l+1] + nums[j] > target:
                    continue
                elif i < r+1 and nums[i] + nums[r-1] + nums[r] + nums[j] < target:
                    continue
                while l < r:
                    arr = [nums[i], nums[l], nums[r], nums[j]]
                    if sum(arr) == target and arr not in result:
                        result.append(arr)
                        l = l + 1
                        r = r - 1
                        while l < r and nums[l] == nums[l-1]:
                            l = l + 1
                        while l < r and nums[r] == nums[r+1]:
                            r = r - 1
                        continue
                    elif sum(arr) < target:
                        l = l + 1
                        while l < r and nums[l] == nums[l-1]:
                            l = l + 1
                        continue
                    elif sum(arr) > target:
                        r = r - 1
                        while l < r and nums[r] == nums[r+1]:
                            r = r - 1
                        continue
        return result


if __name__ == "__main__":
    # print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
    # print(Solution().fourSum([5, 5, 3, 5, 1, -5, 1, -2], 4))
    print(Solution().fourSum([1, -2, -5, -4, -3, 3, 3, 5], -11))