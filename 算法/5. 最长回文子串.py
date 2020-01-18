import numpy as np


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return ""
        max_str = s[0]
        max_len = len(max_str)
        state = np.zeros((len(s), len(s)), dtype=bool)
        for j in range(1, len(s)):
            for i in range(j):
                if (s[i] == s[j]) and ((j-i <= 2) or (state[i+1, j-1])):
                    state[i, j] = True
                if (state[i, j]) and (len(s[i:j+1]) > max_len):
                    max_str = s[i:j+1]
                    max_len = len(max_str)
        return max_str


if __name__ == "__main__":
    # print(Solution().longestPalindrome("babad"))
    # print(Solution().longestPalindrome("cbbd"))
    print(Solution().longestPalindrome("aaaa"))


