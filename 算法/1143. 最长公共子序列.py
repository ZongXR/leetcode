"""
给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

若这两个字符串没有公共子序列，则返回 0。

 

示例 1:

输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace"，它的长度为 3。
示例 2:

输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc"，它的长度为 3。
示例 3:

输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import numpy as np


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        最长公共子序列\n
        :param text1: 第一个字符串
        :param text2: 第二个字符串
        :return: 最长公共子序列长度
        """
        # mat[i, j]表示text1[0:i+1]和text2[0:j+1]的最长公共子序列
        mat = np.zeros((len(text1), len(text2)), dtype=int)
        idx1 = text1.find(text2[0])
        idx2 = text2.find(text1[0])
        if idx1 != -1:
            mat[idx1:, 0] = 1
        if idx2 != -1:
            mat[0, idx2:] = 1
        for i in range(1, mat.shape[0]):
            for j in range(1, mat.shape[1]):
                if text1[i] == text2[j]:
                    mat[i, j] = mat[i - 1, j - 1] + 1
                else:
                    mat[i, j] = max(mat[i - 1, j], mat[i, j - 1])
        return int(np.max(mat))


if __name__ == '__main__':
    print(Solution().longestCommonSubsequence("abcde", "ace"))                  # 3
    print(Solution().longestCommonSubsequence("ace", "abcde"))                  # 3
    print(Solution().longestCommonSubsequence("abc", "abc"))                    # 3
    print(Solution().longestCommonSubsequence("abc", "def"))                    # 0
    print(Solution().longestCommonSubsequence("bl", "yby"))                 # 1
    print(Solution().longestCommonSubsequence("psnw", "vozsh"))                 # 1
    print(Solution().longestCommonSubsequence("bsbininm", "jmjkbkjkv"))                 # 1
    print(Solution().longestCommonSubsequence("oxcpqrsvwf", "shmtulqrypy"))                 # 2
    print(Solution().longestCommonSubsequence("abcba", "abcbcba"))                  # 3
