class Solution:
    def romanToInt(self, s: str) -> int:
        special = {
            "IV": 4, "IX": 9,
            "XL": 40, "XC": 90,
            "CD": 400, "CM": 900,
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }
        result = 0
        lst = list(s)
        while len(lst) > 0:
            temp = ""
            if (len(lst) >= 2) and (lst[0] + lst[1] in special.keys()):
                temp = temp + lst.pop(0)
                temp = temp + lst.pop(0)
                result = result + special[temp]
            else:
                temp = lst.pop(0)
                result = result + special[temp]
        return result
