"""
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:

输入:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2:

输入:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
进阶:

一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个常数空间的解决方案吗

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/set-matrix-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import numpy as np


class Solution:
    def setZeroes(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        result = np.array(matrix)
        new_mat = np.where(self.has_zero(result), 0, result)
        matrix.clear()
        matrix.extend(new_mat.tolist())
        print(matrix)

    def has_zero(self, mat: np.ndarray) -> np.ndarray:
        """
        当前列或行是否有0\n
        :param mat: 原始矩阵
        :return: 是否有0
        """
        result = np.zeros(mat.shape, dtype=int)
        for i in range(0, result.shape[0]):
            for j in range(0, result.shape[1]):
                result[i, j] = np.in1d(mat[i, :], 0).sum() + np.in1d(mat[:, j], 0).sum()
        return result.astype(bool)


if __name__ == '__main__':
    Solution().setZeroes([
        [0,1,2,0],
        [3,4,5,2],
        [1,3,1,5]
    ])