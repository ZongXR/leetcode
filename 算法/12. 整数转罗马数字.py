class Solution:
    def intToRoman(self, num: int) -> str:
        digits = []
        while num > 0:
            digits.append(num % 10)
            num = num // 10
        digits.reverse()
        while len(digits) < 4:
            digits.insert(0, 0)
        special = {
            4: "IV", 9: "IX",
            40: "XL", 90: "XC",
            400: "CD", 900: "CM"
        }
        roma = [('M',), ('C', 'D'), ('X', 'L'), ('I', 'V')]
        result = "M" * digits[-4]
        for i in range(-3, 0):
            if digits[i] == 4:
                result = result + special[4 * (10 ** (-i - 1))]
                continue
            elif digits[i] == 9:
                result = result + special[9 * (10 ** (-i - 1))]
                continue
            elif digits[i] < 4:
                result = result + roma[i][0] * digits[i]
                continue
            elif digits[i] > 4:
                result = result + roma[i][1] + roma[i][0] * (digits[i] - 5)
                continue
        return result
