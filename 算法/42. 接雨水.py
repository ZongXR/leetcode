class Solution:
    def trap(self, height: [int]) -> int:
        if len(height) == 0:
            return 0
        max_height = max(height)
        max_height_idx = height.index(max_height)
        full = height.copy()
        for i in range(0, max_height_idx):
            full[i] = max(height[0:i+1])
        for j in range(-1, -(len(height)-max_height_idx), -1):
            full[j] = max(height[-1:j-1:-1])
        return sum([full[i] - height[i] for i in range(len(height))])


if __name__ == "__main__":
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(Solution().trap([5, 0, 5, 1, 5, 2, 5]))

