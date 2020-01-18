import numpy as np


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == len(p) == 0:
            return True
        elif len(s) == 0 and len(p) > 0:
            return {'*'} == set(p)
        elif len(s) > 0 and len(p) == 0:
            return False
        status = np.zeros((len(s), len(p)), dtype=bool)
        if s[0] == p[0] or p[0] == '.' or p[0] == '?' or p[0] == '*':
            status[0, 0] = True
        for j in range(1, status.shape[1]):
            status[0, j] = status[0, j - 1] and (p[j] == '*' or p[0:j+1].strip('*') == s[0] or p[0:j+1].strip('*') == '?' or p[0:j+1].strip('*') == '.')
        status[1:, 0] = p[0] == '*'
        for i in range(1, status.shape[0]):
            for j in range(1, status.shape[1]):
                if s[i] == p[j] or p[j] == '?' or p[j] == '.':
                    status[i, j] = status[i - 1, j - 1]
                elif p[j] == '*':
                    status[i, j] = status[i - 1, j] or status[i, j - 1]
        return status[-1, -1]


if __name__ == "__main__":
    print(Solution().isMatch("aa", "a"))
    print(Solution().isMatch("aa", "*"))
    print(Solution().isMatch("cb", "?a"))
    print(Solution().isMatch("adceb", "*a*b"))
    print(Solution().isMatch("acdcb", "a*c?b"))
    print(Solution().isMatch("acdcb", "***b"))
    print(Solution().isMatch("abbabbbaabaaabbbbbabbabbabbbabbaaabbbababbabaaabbab", "*aabb***aa**a******aa*"))
    print(Solution().isMatch("mississippi", "m??*ss*?i*pi"))
    print(Solution().isMatch("ho", "**ho"))