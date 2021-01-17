"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
 

示例 1：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
示例 2：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        """
        搜索矩阵\n
        :param matrix: 矩阵
        :param target: 搜索目标
        :return: 是否有该数字
        """
        points = []
        for i in range(0, len(matrix)):
            points.append((matrix[i][0], matrix[i][-1]))
        idx = self.binary_find(points, target)
        if idx == -1:
            return False
        else:
            return self.binary_search(matrix[idx], target)

    def binary_search(self, lst: [int], target: int) -> bool:
        """
        二分查找\n
        :param lst: 列表
        :param target: 要查找的数字
        :return: 是否有该数字
        """
        if len(lst) == 0:
            return False
        if len(lst) == 1:
            if lst[0] == target:
                return True
            else:
                return False
        num = lst[len(lst) // 2]
        if num == target:
            return True
        if num < target:
            return self.binary_search(lst[len(lst) // 2:], target)
        else:
            return self.binary_search(lst[0:len(lst) // 2], target)

    def binary_find(self, lst: [tuple], target: int) -> int:
        """
        二分查找，在哪个区间内\n
        :param lst: 列表
        :param target: 目标
        :return: 区间索引
        """
        idx = len(lst) // 2
        if lst[idx][0] <= target <= lst[idx][1]:
            return idx
        if target > lst[-1][-1] or target < lst[0][0]:
            return -1
        if target > lst[idx][1]:
            inner = self.binary_find(lst[idx:], target)
            if inner != -1:
                return idx + inner
            else:
                return -1
        else:
            return self.binary_find(lst[0:idx], target)


if __name__ == '__main__':
    print(Solution().binary_search([1, 2, 4, 6, 8], 3))
    print(Solution().binary_find([(1, 7), (10, 20), (23, 60)], 21))
    print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
    print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))

