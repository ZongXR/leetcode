import numpy as np


class Solution:
    def rotate(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nums = np.array(matrix)
        matrix.clear()
        matrix.extend(nums.T[:, ::-1].tolist())
        print(matrix)


if __name__ == "__main__":
    Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    Solution().rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])