import re
import numpy as np


class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        partern = re.compile(r"[-|+]?\d*")
        new_str = partern.findall(str)[0]
        try:
            return int(np.clip(int(new_str), -2 ** 31, 2 ** 31 - 1))
        except:
             return 0

