"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        爬楼梯\n
        :param n: 楼梯阶数
        :return: 几种方法可以爬到楼顶
        """
        result = [1, 2]
        if n == 1:
            return 1
        if n == 2:
            return 2
        for i in range(3, n+1):
            result.append(result[-1] + result[-2])
        return result[-1]


if __name__ == '__main__':
    print(Solution().climbStairs(2))
    print(Solution().climbStairs(3))