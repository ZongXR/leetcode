"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import numpy as np


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        有多少种路径\n
        :param m: 行
        :param n: 列
        :return: 多少条路径
        """
        # mat[i, j]表示从i, j开始到结束有多少种走法
        mat = np.zeros((m, n), dtype=int)
        mat[:, 0] = 1
        mat[0, :] = 1
        for i in range(1, m):
            for j in range(1, n):
                mat[i, j] = mat[i - 1, j] + mat[i, j - 1]
        return int(mat[-1, -1])


if __name__ == '__main__':
    print(Solution().uniquePaths(3, 7))
