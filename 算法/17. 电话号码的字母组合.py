class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        if len(digits) < 1:
            return digits
        num_dict = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        result = list(num_dict[digits[0]])
        for x in digits[1:]:
            result = [i + j for i in result for j in num_dict[x]]
        return result


if __name__ == "__main__":
    print(Solution().letterCombinations("23"))
