"""
给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

 

示例 1：

输入：n = 3, k = 3
输出："213"
示例 2：

输入：n = 4, k = 9
输出："2314"
示例 3：

输入：n = 3, k = 1
输出："123"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        排列组合\n
        :param n: 排列数个数
        :param k: 第几个
        :return: 字符串
        """
        if n == 1:
            return "1"
        if k == 1:
            return "".join([str(x) for x in list(range(1, n + 1))])
        k = k - 1
        range_min = self.in_range(k)
        lst = self.to_list(range_min)
        nums = self.jie_cheng(lst[-1])
        route = []
        while len(nums) > 0:
            x = nums.pop()
            route.append(k // x)
            k = k % x
        if len(route) < n - 1:
            route = [0] * (n - 1 - len(route)) + route
        ori_nums = list(range(1, n + 1))
        result = ""
        while len(route) > 0:
            index = route.pop(0)
            result = result + str(ori_nums.pop(index))
        return result + str(ori_nums[0])

    def in_range(self, num: int) -> int:
        """
        计算num落入哪个阶乘区间\n
        :param num: 数字
        :return: 阶乘区间左端点
        """
        i = 1
        j = i * (i + 1)
        temp = 1
        while True:
            if temp <= num < j:
                return temp
            else:
                i = i + 1
                temp = temp * i
                j = temp * (i + 1)

    def to_list(self, num: int) -> [int]:
        """
        将一个数分解成阶乘的形式\n
        :param num: 数字
        :return: 结成列表
        """
        i = 1
        result = []
        temp = i
        if num == 1:
            return [1]
        while True:
            if temp == num:
                return result + [result[-1] + 1]
            else:
                result.append(i)
                i = i + 1
                temp = temp * i

    def jie_cheng(self, num: int) -> [int]:
        """
        计算阶乘，并追加到list后面\n
        :param num: 谁的阶乘
        :return: 列表
        """
        if num == 1:
            return [1]
        if num == 2:
            return [1, 2]
        result = [1]
        for i in range(1, num + 1):
            result.append(result[-1] * (i + 1))
        return result[:-1]


if __name__ == "__main__":
    s = Solution()
    print(s.getPermutation(5, 37))
    # print(s.in_range(37))