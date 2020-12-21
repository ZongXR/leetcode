"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        """
        实现开方\n
        :param x: 要开方的数字
        :return: 结果
        """
        if x == 1 or x == 0:
            return x
        low = 0
        up = x
        while True:
            if up == low or low + 1 == up:
                return low
            low, up = self.get_root(low, up, x)

    def get_root(self, low: int, up: int, num: int) -> (int, int):
        """
        折半查找\n
        :param low: 下限
        :param up: 上限
        :param num: 要开方的数字
        :return: 下限, 上限
        """
        middle = (low + up) // 2
        if middle ** 2 > num:
            return low, middle
        else:
            return middle, up


if __name__ == '__main__':
    print(Solution().mySqrt(2))