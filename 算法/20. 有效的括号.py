class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {
            "(": ")",
            "{": "}",
            "[": "]",
            "<": ">",
        }
        for x in s:
            if x in bracket.keys():
                stack.append(x)
            elif x in bracket.values():
                try:
                    if bracket[stack.pop()] != x:
                        return False
                except IndexError:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    # print(Solution().isValid("([)]"))
    # print(Solution().isValid("{[]}"))
    print(Solution().isValid("["))