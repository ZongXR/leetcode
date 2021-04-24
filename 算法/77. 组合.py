"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combinations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> [[int]]:
        """
        生成组合数\n
        :param n: 从1到n
        :param k: 选k个
        :return: 满足的列表
        """
        result = combinations(range(1, n + 1), r=k)
        return list(map(list, result))


if __name__ == '__main__':
    print(Solution().combine(4, 2))