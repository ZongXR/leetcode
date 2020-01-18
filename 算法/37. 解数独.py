# %% 导入包
import numpy as np
from 有效的数独 import Solution as Solve


class Solution:
    def solveSudoku(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        array = Solve().get_array(board)
        idx = self.get_loc(array)
        nums = self.get_available(array, idx)
        flag = self.fill_num(array, idx, nums)
        print(array)
        board.clear()
        board.extend(array.astype(str).tolist())

    # 填入数字
    def fill_num(self, array, idx, nums):
        stack_idx = []
        stack_nums = []
        try:
            while 0 in array:
                if len(nums) == 0:
                    idx = stack_idx.pop()
                    nums = stack_nums.pop()
                    array[idx] = 0
                else:
                    array[idx] = nums.pop()
                    stack_idx.append(idx)
                    stack_nums.append(nums)
                    idx = self.get_loc(array)
                    nums = self.get_available(array, idx)
            return True
        except IndexError:
            return False

    # 获取填入位置
    def get_loc(self, array):
        constraints_num = self.calc_constraints(array)
        idx_i, idx_j = np.where(constraints_num == constraints_num.max())
        return idx_i[0], idx_j[0]

    # 计算每个缺失位置的约束数
    def calc_constraints(self, array):
        array_bool = array.astype(bool)
        # 每一行的非零数
        array_bool_col = array_bool.sum(axis=0, keepdims=True)
        # 每一列的非零数
        array_bool_row = array_bool.sum(axis=1, keepdims=True)
        # 每一个九宫格的非零数
        array_bool_box = np.zeros((3, 3), dtype=int)
        for i in range(3):
            for j in range(3):
                array_bool_box[i, j] = array_bool[3*i:3*(i+1), 3*j:3*(j+1)].sum()
        array_bool_box = array_bool_box.repeat(3, axis=0).repeat(3, axis=1)
        # 计算每个元素的约束数
        result = array_bool_row + array_bool_col + array_bool_box
        array_bool_no = 1 - array_bool
        return array_bool_no * result

    # 获取可填数字
    def get_available(self, array, idx):
        one_row = set(array[idx[0], :].tolist())
        one_col = set(array[:, idx[1]].tolist())
        row_start, row_end, col_start, col_end = Solve().get_box(idx[0], idx[1])
        one_box = set(array[row_start:row_end+1, col_start:col_end+1].ravel().tolist())
        num_set = {x for x in one_row | one_col | one_box if x != 0}
        available = set(range(1, 10)) - num_set
        return available


if __name__ == "__main__":
    test = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    Solution().solveSudoku(test)
    print(test)

