import numpy as np


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        my_tab = np.zeros((numRows, len(s)), dtype=np.str)
        i = 0
        i_value = [num for num in range(numRows)] + [num for num in range(numRows - 2, 0, -1)]
        for x in s:
            my_tab[i_value[i % len(i_value)], i] = x
            i = i + 1
        return ''.join(my_tab.ravel().tolist())
