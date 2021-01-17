"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意：请不要使用代码库中的排序函数来解决这道题。

 

进阶：

你能想出一个仅使用常数空间的一趟扫描算法吗？
 

示例 1：

输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]
示例 2：

输入：nums = [2,0,1]
输出：[0,1,2]
示例 3：

输入：nums = [0]
输出：[0]
示例 4：

输入：nums = [1]
输出：[1]
 

提示：

n == nums.length
1 <= n <= 300
nums[i] 为 0、1 或 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-colors
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from copy import deepcopy


class Solution:
    def sortColors(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result = self.quick_sort(nums)
        nums.clear()
        nums.extend(result)
        print(nums)

    def quick_sort(self, nums: [int]) -> [int]:
        """
        快速排序\n
        :param nums: 要排序的数组
        :return: 排序后的数组
        """
        if len(nums) == 0 or len(nums) == 1:
            return deepcopy(nums)
        if len(nums) == 2:
            return sorted(nums)
        idx = len(nums) // 2
        num = nums[idx]
        left = []
        right = []
        it = []
        for x in nums:
            if x < num:
                left.append(x)
            elif x > num:
                right.append(x)
            else:
                it.append(x)
        return self.quick_sort(left) + it + self.quick_sort(right)


if __name__ == '__main__':
    Solution().sortColors([2, 0, 2, 1, 1, 0])
    Solution().sortColors([2, 0, 1])
    Solution().sortColors([0])