"""
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

 

示例 1：


输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
示例 2：

输入：grid = [[1,2,3],[4,5,6]]
输出：12

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import numpy as np


class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        """
        求最小路径\n
        :param grid: 地图
        :return: 最小长度
        """
        mat = np.array(grid, dtype=int)
        if mat.shape[0] == 1 or mat.shape[1] == 1:
            return int(mat.sum())
        # result[i, j]表示从mat[-1-i, -1-j]到结束点的距离
        result = np.zeros(mat.shape, dtype=int)
        for i in range(0, result.shape[0]):
            for j in range(0, result.shape[1]):
                if i == 0 and j == 0:
                    result[i, j] = mat[-1, -1]
                    continue
                if i == 0:
                    result[i, j] = mat[-1-i, -1-j] + result[i, j - 1]
                    continue
                if j == 0:
                    result[i, j] = mat[-1-i, -1-j] + result[i - 1, j]
                    continue
                result[i, j] = mat[-1-i, -1-j] + min(result[i, j - 1], result[i - 1, j])
        return int(result[-1, -1])


if __name__ == '__main__':
    print(Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
    print(Solution().minPathSum([[1, 2, 3], [4, 5, 6]]))

