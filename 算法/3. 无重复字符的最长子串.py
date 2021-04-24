"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

 

示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        my_lst = list(s)
        new_lst = []
        result = 0
        max_len = 0
        while len(my_lst) > 0:
            x = my_lst.pop(0)
            if x not in new_lst:
                new_lst.append(x)
                max_len = max_len + 1
            else:
                idx = new_lst.index(x)
                new_lst = new_lst[idx:]
                new_lst.pop(0)
                new_lst.append(x)
                max_len = len(new_lst)
            result = max(result, max_len)
        return result

