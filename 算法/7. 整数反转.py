class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            return int(str(x)[::-1]) if self.check(int(str(x)[::-1])) else 0
        else:
            return -int(str(-x)[::-1]) if self.check(-int(str(-x)[::-1])) else 0

    def check(self, x):
        if -2 ** 31 <= x <= 2 ** 31 - 1:
            return x
        else:
            return 0
        