"""
给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

 

示例 1：

输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
示例 2：

输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insert-interval
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def insert(self, intervals: [[int]], newInterval: [int]) -> [[int]]:
        """
        寻找左边界右边界\n
        :param intervals:
        :param newInterval:
        :return: 新的区间段
        """
        results = []
        x = newInterval[0]
        y = newInterval[1]
        if len(intervals) == 0:
            return [newInterval]
        xx = x
        yy = y
        while len(intervals) > 0:
            interval = intervals.pop(0)
            if interval[0] <= interval[1] < x:
                # 如果没覆盖住，则没有交集
                results.append(interval)
            elif x < interval[0] <= interval[1]:
                # 如果完全覆盖住了，则塞回去
                intervals.insert(0, interval)
                break
            else:
                # 如果有交集
                xx = min(xx, interval[0])
                yy = max(yy, interval[1])
                break

        while len(intervals) > 0:
            interval = intervals.pop(-1)
            if y < interval[0] <= interval[1]:
                # 如果没覆盖住，则没有交集
                results.append(interval)
            elif interval[0] <= interval[1] < y:
                # 如果完全覆盖住，则塞回去
                intervals.append(interval)
                break
            else:
                # 如果有交集
                xx = min(xx, interval[0])
                yy = max(yy, interval[1])
                break
        results.append([xx, yy])
        return sorted(results)


if __name__ == "__main__":
    # print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8]))
    # print(Solution().insert([[1, 5]], [2, 3]))
    # print(Solution().insert([[1, 3], [6, 9]], [2, 5]))
    # print(Solution().insert([[1, 5]], [0, 3]))
    print(Solution().insert([[0, 1], [5, 5], [6, 7], [9, 11]], [12, 21]))
