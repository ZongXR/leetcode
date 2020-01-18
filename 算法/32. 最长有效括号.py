class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        result = 0
        for idx, x in enumerate(s):
            if x == "(":
                stack.append(idx)
            elif x == ")":
                stack.pop()
                if len(stack) == 0:
                    stack.append(idx)
                else:
                    result = max(result, idx - stack[-1])
        return result


if __name__ == "__main__":
    print(Solution().longestValidParentheses(")()())"))
    print(Solution().longestValidParentheses("(()"))
    print(Solution().longestValidParentheses(""))
    print(Solution().longestValidParentheses("((((("))
    print(Solution().longestValidParentheses("()(()"))
    print(Solution().longestValidParentheses("))))())()()(()"))
