# -*- coding: utf-8 -*-
"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
"""
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        flag = False
        result = s
        i = 0
        while i < len(s):
            if s[i] in t:
                break
            i = i + 1
        j = i + len(t)
        letters_need = self.get_dict(s[i:j], t)
        while i < len(s) and j < len(s):
            if len(s[i:]) < len(t):
                # 覆盖不住了
                break
            if s[i] in t and j < i + len(t):
                j = i + len(t)
                letters_need = self.get_dict(s[i:j], t)
            if s[i] in t and s[j - 1] in t and self.is_ok(letters_need):
                # 如果正好碰上了
                result = s[i:j] if len(s[i:j]) < len(result) else result
                flag = True
                i = i + 1
                # 左边界，原来有的被吐出来了，要加上
                letters_need[s[i - 1]] = letters_need[s[i - 1]] + 1
                while i < len(s):
                    if s[i] in t:
                        break
                    i = i + 1
            else:
                j = j + 1
                # 右边界，原来没有的，被囊括进来的，需要减去
                if j <= len(s) and s[j - 1] in t:
                    letters_need[s[j - 1]] = letters_need[s[j - 1]] - 1
        while i < len(s) and j <= len(s) and s[j - 1] in t:
            if len(s[i:]) < len(t):
                break
            if s[i] in t and s[j - 1] in t and self.is_ok(letters_need):
                result = s[i:j] if len(s[i:j]) < len(result) else result
                flag = True
                i = i + 1
                letters_need[s[i - 1]] = letters_need[s[i - 1]] + 1
            else:
                i = i + 1
        return result if flag else ""

    def get_dict(self, s: str, t: str) -> dict:
        """
        获取字典\n
        :param s: 第一个字符串
        :param t: 第二个字符串
        :return: 一个字典
        """
        cnt_s = Counter(s)
        cnt_t = Counter(t)
        result = dict()
        for letter in cnt_t.keys():
            result[letter] = cnt_t[letter] - cnt_s[letter]
        return result

    def is_ok(self, letters: dict) -> bool:
        """
        是否满足条件\n
        :param letters: 需求
        :return: 是否满足
        """
        for k, v in letters.items():
            if v > 0:
                return False
        return True


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    s = "a"
    t = "a"
    s = "a"
    t = "aa"
    s = "a"
    t = "b"
    s = "bba"
    t = "ab"
    s = "acbbaca"
    t = "aba"
    s = "ab"
    t = "a"
    s = "abc"
    t = "b"
    s = "abc"
    t = "ab"
    s = "bbaac"
    t = "aba"
    print(Solution().minWindow(s, t))