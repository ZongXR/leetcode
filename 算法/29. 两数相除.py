import numpy as np


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            raise ZeroDivisionError
        elif dividend == 0:
            return 0
        # flag为True表示结果是负数
        flag = (dividend > 0) ^ (divisor > 0)
        result = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = dividend
        lst = []
        while res >= divisor:
            i = 0
            while res > 0:
                i = i + 1
                res = dividend - (divisor << i)
            i = i - 1
            res = dividend - (divisor << i)
            lst.append(i)
            dividend = res
        for x in lst:
            result = result + 2 ** x
        if flag:
            return int(np.clip(-result, -2**31, 2**31 - 1))
        else:
            return int(np.clip(result, -2**31, 2**31 - 1))


if __name__ == "__main__":
    print(Solution().divide(7, -3))
    print(Solution().divide(-2147483648, -1))
    print(Solution().divide(1, 1))