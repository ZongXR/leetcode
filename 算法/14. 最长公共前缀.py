class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        result = ""
        if len(strs) == 0:
            return result
        elif len(strs) == 1:
            return strs[0]
        elif len(set(strs)) == 1:
            return strs[0]
        words = [list(word) for word in strs]
        wordsT = list(zip(*words))
        for item in wordsT:
            if len(set(item)) == 1:
                result = result + item[0]
            else:
                break
        return result


