class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.str2num(num1) * self.str2num(num2))

    # 字符串转数字
    def str2num(self, num: str) -> int:
        result = 0
        for i, x in enumerate(num[::-1]):
            result = result + int(x) * 10 ** i
        return result


if __name__ == "__main__":
    print(Solution().multiply("123", "456"))
