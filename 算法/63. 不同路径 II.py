"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？



网格中的障碍物和空位置分别用 1 和 0 来表示。

 

示例 1：


输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
示例 2：


输入：obstacleGrid = [[0,1],[0,0]]
输出：1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import numpy as np


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
        """
        有障碍物有多少条路径\n
        :param obstacleGrid:
        :return:
        """
        grid = np.array(obstacleGrid)
        if grid[0, 0] > 0:
            return 0
        mat = np.zeros(grid.shape, dtype=int)
        mat[:, 0] = 1
        mat[0, :] = 1
        if grid[-1, -1] == 1:
            return 0
        for i in range(mat.shape[0]):
            if grid[-1-i, -1] == 0:
                mat[i, 0] = 1
            else:
                mat[i:, 0] = 0
                break
        for i in range(mat.shape[1]):
            if grid[-1, -1-i] == 0:
                mat[0, i] = 1
            else:
                mat[0, i:] = 0
                break
        for i in range(1, mat.shape[0]):
            for j in range(1, mat.shape[1]):
                if grid[-1-i+1, -1-j] == 1:
                    mat[i - 1, j] = 0
                if grid[-1-i, -1-j+1] == 1:
                    mat[i, j - 1] = 0
                mat[i, j] = mat[i - 1, j] + mat[i, j - 1]
        return int(mat[-1, -1])


if __name__ == '__main__':
    print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(Solution().uniquePathsWithObstacles([[0, 1], [0, 0]]))
    print(Solution().uniquePathsWithObstacles([[0, 0], [1, 1], [0, 0]]))