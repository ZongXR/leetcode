"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        """
        螺旋矩阵\n
        :param matrix: 原始矩阵
        :return: 顺时针展开
        """
        result = []
        while len(matrix) > 1:
            result.extend(matrix[0])
            matrix = self.trans(matrix[1:])
        result.extend(matrix[0])
        return result

    def trans(self, matrix: [[int]]) -> [[int]]:
        """
        矩阵转置
        :param matrix: 原始矩阵
        :return: 转置后的矩阵
        """
        return list(zip(*matrix))[::-1]


if __name__ == "__main__":
    mat = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print(Solution().spiralOrder(mat))


