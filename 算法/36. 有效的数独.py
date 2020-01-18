import numpy as np


class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        array = self.get_array(board)
        for i in range(array.shape[0]):
            for j in range(array.shape[1]):
                if array[i, j] == 0:
                    continue
                index_rows = np.where(array[i, :] == array[i, j])[0]
                index_cols = np.where(array[:, j] == array[i, j])[0]
                box = array[self.get_box(i, j)[0]:self.get_box(i, j)[1]+1, self.get_box(i, j)[2]:self.get_box(i, j)[3]+1]
                index_box = np.where(box == array[i, j])
                if len(index_rows) == 1 and len(index_cols) == 1 and len(index_box[0]) == 1 and len(index_box[1] == 1):
                    continue
                else:
                    return False
        return True

    def get_array(self, board: [[str]]) -> np.ndarray:
        temp = np.array(board)
        temp2 = np.where(temp == ".", 0, temp)
        return temp2.astype(int)

    def get_box(self, i, j):
        times_i = i // 3
        times_j = j // 3
        return 3 * times_i, 3 * times_i + 2, 3 * times_j, 3 * times_j + 2


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
    # print(Solution().get_array(test))
    print(Solution().isValidSudoku(test))
