# -*- coding: utf-8 -*-
"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
"""
from copy import deepcopy


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        original_letters = self.get_dict(t)
        global_flag = False
        result = s
        i = 0
        while i < len(s):
            letters = deepcopy(original_letters)
            if s[i] in t:
                letters[s[i]] = letters[s[i]] - 1 if letters[s[i]] - 1 >= 0 else 0
                j = i
                flag = False
                while j < len(s):
                    if i != j and s[j] in t:
                        letters[s[j]] = letters[s[j]] - 1 if letters[s[j]] - 1 >= 0 else 0
                    j = j + 1
                    if sum(letters.values()) == 0:
                        flag = True
                        global_flag = True
                        break
                result = s[i:j] if len(s[i:j]) < len(result) and flag else result
                i = i + 1
            else:
                i = i + 1
        return result if global_flag else ""


    def get_dict(self, t: str) -> dict:
        """
        将字符串转为字典\n
        :param t: 字符串
        :return:  字典
        """
        result = dict()
        for letter in set(list(t)):
            result[letter] = t.count(letter)
        return result


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    # s = "a"
    # t = "a"
    # s = "a"
    # t = "aa"
    # s = "a"
    # t = "b"
    print(Solution().minWindow(s, t))