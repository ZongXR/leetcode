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

