"""
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import numpy as np


class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        """
        螺旋矩阵\n
        :param n: 矩阵中最大的数
        :return: 矩阵
        """
        i = 0
        j = 0
        direction = 0
        result = np.zeros((n, n), dtype=int)
        nums = list(range(1, n ** 2 + 1))
        while len(nums) > 0:
            num = nums.pop(0)
            result[i, j] = num
            i, j, direction = self.get_direction([i, j, direction], result)
        return result.tolist()

    def get_direction(self, loc: [int], mat: np.ndarray) -> [int]:
        """
        获得方向\n
        :param loc: i, j, direction
        :param mat: 矩阵
        :return: i, j, direction
        """
        direction = loc.pop()
        if direction == 0:
            i = loc[0]
            j = loc[1] + 1
            if j >= mat.shape[1] or mat[i, j] != 0:
                i = loc[0] + 1
                j = loc[1]
                direction = 1
            return i, j, direction
        elif direction == 1:
            i = loc[0] + 1
            j = loc[1]
            if i >= mat.shape[0] or mat[i, j] != 0:
                i = loc[0]
                j = loc[1] - 1
                direction = 2
            return i, j, direction
        elif direction == 2:
            i = loc[0]
            j = loc[1] - 1
            if j < 0 or mat[i, j] != 0:
                i = loc[0] - 1
                j = loc[1]
                direction = 3
            return i, j, direction
        elif direction == 3:
            i = loc[0] - 1
            j = loc[1]
            if i < 0 or mat[i, j] != 0:
                i = loc[0]
                j = loc[1] + 1
                direction = 0
            return i, j, direction


if __name__ == "__main__":
    print(Solution().generateMatrix(3))
