"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import numpy as np
from typing import Optional, Set
from copy import deepcopy


class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        """
        是否存在字符串\n
        :param board: 网格
        :param word: 字符串
        :return: 是否存在
        """
        word = word[::-1]
        if not self.contains(board, word):
            return False
        routes = {tuple()}
        board = np.array(board)
        for letter in word:
            next_routes = set()
            for current_route in routes:
                current_loc = None if len(current_route) == 0 else current_route[-1]
                neighbors = self.get_neighbors(board, current_loc, letter)
                neighbors = list(filter(lambda x: x not in current_route, neighbors))
                if len(neighbors) > 0:
                    for neighbor in neighbors:
                        next_routes.add(current_route + (neighbor, ))
            if len(next_routes) > 0:
                routes = deepcopy(next_routes)
            else:
                return False
        return True

    def get_neighbors(self, board: np.ndarray, current_loc: Optional[tuple], letter: str) -> [tuple]:
        """
        获取邻居\n
        :param board: 网格
        :param current_loc: 当前位置
        :param letter: 要找的字符
        :return: 邻居
        """
        xs, ys = np.where(board == letter)
        xs = xs.tolist()
        ys = ys.tolist()
        xy = list(zip(xs, ys))
        if current_loc is None:
            return xy
        else:
            return list(filter(lambda x: self.is_neighbor(current_loc, x), xy))

    @staticmethod
    def is_neighbor(loc1: tuple, loc2: tuple) -> bool:
        """
        是否是相邻的\n
        :param loc1: 位置1
        :param loc2: 位置2
        :return: 是否相邻
        """
        x1, y1 = loc1
        x2, y2 = loc2
        return (abs(x2 - x1) == 1 and y1 == y2) or (abs(y2 - y1) == 1 and x1 == x2)

    @staticmethod
    def contains(board: [[str]], word: str):
        """
        判断字符个数是否相等\n
        :param board: 网格
        :param word: 单词
        :return: 是否相等
        """
        letters = "".join(["".join(x) for x in board])
        unique_letters = set(list(word))
        for unique_letter in unique_letters:
            if letters.count(unique_letter) < word.count(unique_letter):
                return False
        return True


if __name__ == '__main__':
    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # word = "ABCCED"
    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # word = "SEE"
    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # word = "ABCB"
    # board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
    # word = "AAAAAAAAAAAAAAB"
    board = [["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "B"], ["A", "A", "A", "A", "B", "A"]]
    word = "AAAAAAAAAAAAABB"
    print(Solution().exist(board, word))

