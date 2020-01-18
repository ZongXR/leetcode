class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        if n == 0:
            return [""]
        elif n == 1:
            return ["()"]
        elif n == 2:
            return ["()()", "(())"]
        result = []
        for i in range(n):
            j = n - 1 - i
            temp1 = self.generateParenthesis(i)
            temp2 = self.generateParenthesis(j)
            result.extend(["(%s)%s" % (p, q) for p in temp1 for q in temp2])
        return result


if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
    print(Solution().generateParenthesis(4))