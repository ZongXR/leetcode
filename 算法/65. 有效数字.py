"""
验证给定的字符串是否可以解释为十进制数字。

例如:

"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import re


class Solution:
    def isNumber(self, s: str) -> bool:
        """
        是否有效数字\n
        :param s: 字符串
        :return: 是否有效
        """
        s = self.pre_process(s)
        pattern = re.compile("^[\\+\\-]?[0-9]+(\\.)?([0-9]+)*(e[\\+\\-]?[0-9]+)?$")
        return bool(re.match(pattern, s.strip()))

    def pre_process(self, s: str) -> str:
        """
        字符串预处理\n
        :param s: 原始字符串
        :return:  处理后的字符串
        """
        result = s.strip()
        pattern = re.compile("^[\\+\\-]?\\.[0-9]+")
        if re.match(pattern, result):
            return result.replace(".", "0.")
        else:
            return result


if __name__ == '__main__':
    print(Solution().isNumber("e") is False)    # False
    print(Solution().isNumber("01") is True)   # True
    print(Solution().isNumber("0") is True)    # True
    print(Solution().isNumber("0.") is True)   # True
    print(Solution().isNumber("00") is True)   # True
    print(Solution().isNumber("0..") is False)  # False
    print(Solution().isNumber(" ") is False)    # False
    print(Solution().isNumber(".") is False)    # False
    print(Solution().isNumber(".e1") is False)  # False
    print(Solution().isNumber("0e1") is True)  # True
    print(Solution().isNumber("e9") is False)   # False
    print(Solution().isNumber("O62") is False)  # False
    print(Solution().isNumber("Se6") is False)  # False
    print(Solution().isNumber(".1") is True)
    print(Solution().isNumber("+.8") is True)
    print(Solution().isNumber(" 005047e+6") is True)
