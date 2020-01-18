class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
        nums.sort()
        result_new = [nums[0], nums[1], nums[-1]]
        dist = abs(target) + sum(map(abs, nums))
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                result = [nums[i], nums[j], nums[k]]
                new_dist = target - sum(result)
                if new_dist == 0:
                    return target
                elif new_dist > 0:
                    if abs(new_dist) < abs(dist):
                        result_new = [nums[i], nums[j], nums[k]]
                        dist = new_dist
                    j = j + 1
                    while j < k and nums[j] == nums[j-1]:
                        j = j + 1
                    continue
                elif new_dist < 0:
                    if abs(new_dist) < abs(dist):
                        result_new = [nums[i], nums[j], nums[k]]
                        dist = new_dist
                    k = k - 1
                    while j < k and nums[k] == nums[k+1]:
                        k = k - 1
                    continue
        return sum(result_new)


if __name__ == "__main__":
    nums = [1, 1, -1, -1, 3]
    target = -1
    print(Solution().threeSumClosest(nums, target))