"""
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

 

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-binary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        二进制求和\n
        :param a: 第一个二进制串
        :param b: 第二个二进制串
        :return: 结果
        """
        nums1 = list(map(int, a[::-1]))
        nums2 = list(map(int, b[::-1]))
        last_digit = 0
        max_length = len(nums1) if len(nums1) > len(nums2) else len(nums2)
        nums1 = nums1 + [0] * (max_length - len(nums1))
        nums2 = nums2 + [0] * (max_length - len(nums2))
        results = []
        for i, num1 in enumerate(nums1):
            num2 = nums2[i]
            result = num1 + num2 + last_digit
            if result < 2:
                last_digit = 0
                results.append(result)
            else:
                last_digit = 1
                results.append(result - 2)
        if last_digit > 0:
            results.append(last_digit)
        return "".join(list(map(str, results[::-1])))


if __name__ == '__main__':
    print(Solution().addBinary("11", "1"))
    print(Solution().addBinary("1010", "1011"))
    print(Solution().addBinary("1111", "1111"))


