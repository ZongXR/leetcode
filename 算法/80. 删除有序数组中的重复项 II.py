# -*- coding: utf-8 -*-
"""
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 最多出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

 

说明：

为什么返回数值是整数，但输出的答案是数组呢？

请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        """
        移除重复的元素\n
        :param nums: 数组
        :return: 长度
        """
        if len(nums) <= 2:
            return len(nums)
        count = len(nums) - 1
        record = 0
        last = None
        i = 0
        while count > 0 and (last is None or nums[i] >= last):
            if last == nums[i] and record >= 2:
                # 需要移位了
                x = nums.pop(i)
                nums.append(x)
                count = count - 1
            else:
                if last == nums[i] and record < 2:
                    # 来了一个相同字符
                    record = record + 1
                    last = nums[i]
                    count = count - 1
                    i = i + 1
                else:
                    # 来了一个新字符
                    record = 1
                    count = count - 1
                    last = nums[i]
                    i = i + 1
        if count == 0 and nums[i] == nums[i - 1] == nums[i - 2]:
            i = i - 1
        return i + 1


if __name__ == '__main__':
    # a = [1,1,1,2,2,3]
    # a = [0,0,1,1,1,1,2,3,3]
    # a = [1, 1, 1]
    a = [1, 2, 2]
    s = Solution().removeDuplicates(a)
    print(a[0:s])
