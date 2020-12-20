"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

 

示例 1：

输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
示例 2：

输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。
示例 3：

输入：digits = [0]
输出：[1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/plus-one
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        """
        加一\n
        :param digits: 原始数字
        :return: 加一后的数字
        """
        last_digit = 0
        temp = digits[::-1]
        for i, num in enumerate(temp):
            new_num = num + int(i == 0) + last_digit
            if new_num < 10:
                temp[i] = new_num
                last_digit = 0
                break
            else:
                temp[i] = new_num - 10
                last_digit = 1
        if last_digit == 0:
            return temp[::-1]
        else:
            return [1] + temp[::-1]


if __name__ == '__main__':
    print(Solution().plusOne([1, 2, 3]))
    print(Solution().plusOne([8, 9, 9]))
    print(Solution().plusOne([9, 9, 9]))
