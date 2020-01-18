class Solution:
    def jump(self, nums: [int]) -> int:
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            return 1
        result = 0
        i = 0
        max_distance = 0
        end = 0
        while True:
            if nums[i] >= len(nums[i+1:]):
                return result + 1
            max_distance = max(max_distance, nums[i] + i)
            # 不管是从哪跳的，反正上次跳最远只能跳到max_distance
            # 一旦到达边界，就将上一轮能达到的最远额距离更新为新的边界
            if i == end:
                end = max_distance
                result = result + 1
            i = i + 1


if __name__ == "__main__":
    print(Solution().jump([2, 3, 1, 1, 4]))
    print(Solution().jump([3, 2, 1]))
    print(Solution().jump([1, 2, 3]))
    print(Solution().jump([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]))