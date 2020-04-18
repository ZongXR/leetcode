import numpy as np
from copy import deepcopy


class Solution:
    def solveNQueens(self, n: int) -> [[str]]:
        mats = []
        locations = []
        for i in range(n):
            mat = np.zeros((n, n), dtype=int)
            mat[0, i] = 1
            mats.append(mat)
            loc = np.ones((n, n), dtype=bool)
            new_loc = self.set_loc(loc, (0, i), False)
            locations.append(new_loc)
        for i in range(n-1):
            mats, locations = self.multi_fill(mats, locations)
        result = []
        [result.append(self.mat2str(x)) for x in mats if self.mat2str(x) not in result]
        return result

    def multi_fill(self, mats: [np.ndarray], loc: [np.ndarray]) -> ([np.ndarray], [np.ndarray]):
        """
        多次填充\n
        :param mats: 矩阵列表
        :param loc: 可填入位置矩阵
        :return: (矩阵列表, 可填入位置矩阵)
        """
        results_mat = []
        results_loc = []
        for i in range(len(mats)):
            result_mat, result_loc = self.fill(mats[i], loc[i])
            results_mat.extend(result_mat)
            results_loc.extend(result_loc)
        return results_mat, results_loc

    def mat2str(self, mat: np.ndarray) -> [str]:
        """
        把矩阵转换成列表字符串\n
        :param mat: 矩阵
        :return: 字符串列表
        """
        mat_str = np.zeros(mat.shape, dtype=str)
        mat_str[mat == 0] = '.'
        mat_str[mat == 1] = 'Q'
        mat_lst = mat_str.tolist()
        return [''.join(x) for x in mat_lst]

    def fill(self, mat: np.ndarray, loc: np.ndarray) -> ([np.ndarray], [np.ndarray]):
        """
        填充矩阵一步\n
        :param mat: 矩阵
        :param loc: 可填充的位置
        :return: (矩阵列表, 可填充位置列表)
        """
        result_mats = []
        result_loc = []
        xs, ys = np.where(loc == True)
        if len(xs) == 0:
            return result_mats, result_loc
        lines = mat.sum()
        mask = xs == lines
        xs = xs[mask]
        ys = ys[mask]
        for i in range(len(xs)):
            new_mat = deepcopy(mat)
            new_mat[xs[i], ys[i]] = 1
            result_mats.append(new_mat)
            new_loc = deepcopy(loc)
            news_loc = self.set_loc(new_loc, (xs[i], ys[i]), False)
            result_loc.append(news_loc)
        return result_mats, result_loc

    def set_loc(self, loc: np.ndarray, xy: (int, int), value: bool) -> np.ndarray:
        """
        设置同行同列童斜线元素位置\n
        :param loc: 位置矩阵
        :param xy: 点坐标
        :param value: 元素值
        :return: 可填充的位置
        """
        loc[xy[0], :] = value
        loc[:, xy[1]] = value
        diag_loc = self.get_tri(loc.shape[0], xy, value)
        return loc & diag_loc

    def get_tri(self, n: int, xy: (int, int), value: bool) -> np.ndarray:
        """
        获取斜线位置矩阵\n
        :param n:
        :param xy:
        :param value:
        :return:
        """
        main_diag = np.tri(n, n, xy[1] - xy[0]) - np.tri(n, n, xy[1] - xy[0] - 1)
        para_diag = np.fliplr(np.tri(n, n, n - sum(xy) - 1) - np.tri(n, n, n - sum(xy) - 2))
        result = np.array(main_diag + para_diag, dtype=bool)
        if value:
            return result
        else:
            return ~result


if __name__ == '__main__':
    # print(Solution().get_tri(5, (3, 2), False))
    test = Solution().solveNQueens(8)
    print(len(test))
