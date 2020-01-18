class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        candidates.sort()
        result = []
        if len(candidates) == 0:
            return result
        elif len(candidates) == 1:
            if target % candidates[0] == 0:
                return [[candidates[0] for _ in range(target // candidates[0])]]
            else:
                return result
        else:
            self.dfs(candidates, target, [], result)
            temp = []
            [temp.append(sorted(x)) for x in result if sorted(x) not in temp]
            return temp

    # 深度优先搜索
    def dfs(self, candidates: [int], target: int, stack: [int], result: [[int]]):
        for x in candidates:
            if x > target:
                break
            stack.append(x)
            child = target - x
            if child == 0:
                result.append(stack.copy())
                stack.pop()
                break
            elif child < min(candidates):
                stack.pop()
            else:
                self.dfs(candidates, child, stack, result)
                stack.pop()


if __name__ == "__main__":
    print(Solution().combinationSum([2, 3], 5))
    print(Solution().combinationSum([1, 2], 1))
    print(Solution().combinationSum([1], 2))
    print(Solution().combinationSum([1], 1))
    print(Solution().combinationSum([2, 3, 6, 7], 7))
    print(Solution().combinationSum([2, 3, 5], 8))


