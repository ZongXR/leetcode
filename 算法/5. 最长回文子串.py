"""
给你一个字符串 s，找到 s 中最长的回文子串。

 

示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
示例 3：

输入：s = "a"
输出："a"
示例 4：

输入：s = "ac"
输出："a"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


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


