class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        num = nums1 + nums2
        num.sort()
        return self.get_median(num)

    def get_median(self, lst):
        if len(lst) % 2 == 0:
            return (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2
        else:
            return lst[len(lst) // 2]