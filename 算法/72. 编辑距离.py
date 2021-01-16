"""
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
 

示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
 

提示：

0 <= word1.length, word2.length <= 500
word1 和 word2 由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import numpy as np


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        最小编辑距离\n
        :param word1: 第一个单词
        :param word2: 第二个单词
        :return: 最小距离
        """
        if word1 == word2:
            return 0
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        result = np.zeros((len(word1), len(word2)), dtype=int)
        if word1[0] == word2[0]:
            result[0, 0] = 0
        else:
            result[0, 0] = 1
        for i in range(0, result.shape[0]):
            for j in range(0, result.shape[1]):
                if i == 0 and j == 0:
                    continue
                if i == 0 and j > 0:
                    result[i, j] = j + 1 if word1[i] not in word2[0:j + 1] else j
                    continue
                if j == 0 and i > 0:
                    result[i, j] = i + 1 if word2[j] not in word1[0:i + 1] else i
                    continue
                if word1[i] == word2[j]:
                    result[i, j] = result[i - 1, j - 1]
                else:
                    result[i, j] = min(result[i, j - 1], result[i - 1, j], result[i - 1, j - 1]) + 1
        return int(result[-1, -1])


if __name__ == '__main__':
    print(Solution().minDistance("intention", "execution"))
    print(Solution().minDistance("horse", "ros"))
    print(Solution().minDistance("a", "b"))
    print(Solution().minDistance("sea", "eat"))
