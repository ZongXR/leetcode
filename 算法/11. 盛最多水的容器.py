class Solution:
    def maxArea(self, height: [int]) -> int:
        result = 0
        i = 0
        j = len(height) - 1
        while j > i:
            volume = (j - i) * min(height[i], height[j])
            result = max(result, volume)
            if height[j] > height[i]:
                i = i + 1
            else:
                j = j - 1
        return result

