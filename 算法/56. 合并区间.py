"""
给出一个区间的集合，请合并所有重叠的区间。

 

示例 1:

输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: intervals = [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        """
        合并区间段\n
        :param intervals: 区间段
        :return: 合并后的区间段
        """
        results = []
        intervals.sort()
        interval = []
        while len(intervals) > 0:
            if len(interval) == 0:
                interval.extend(intervals.pop(0))
            else:
                interval_new = intervals.pop(0)
                if max(interval) >= min(interval_new):
                    # 如果二者有交叉
                    interval.extend(interval_new)
                else:
                    results.append([min(interval), max(interval)])
                    interval = interval_new
        results.append([min(interval), max(interval)])
        return results


if __name__ == "__main__":
    print(Solution().merge([[1, 4], [4, 5]]))

