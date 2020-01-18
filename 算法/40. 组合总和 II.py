class Solution:
    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        result = []
        if len(candidates) == 0:
            return result
        elif sum(candidates) < target:
            return []
        elif sum(candidates) == target:
            return [candidates]
        else:
            self.dfs(candidates, target, [], result)
            temp = []
            [temp.append(sorted(x)) for x in result if sorted(x) not in temp]
            return temp

    # 深度优先搜索
    def dfs(self, candidates: [int], target: int, stack: [int], result: [[int]]):
        for x in sorted(candidates.copy()):
            if x > target:
                break
            stack.append(candidates.pop(candidates.index(x)))
            child = target - x
            if child == 0:
                result.append(stack.copy())
                candidates.append(stack.pop(stack.index(x)))
            elif child < min(candidates):
                candidates.append(stack.pop(stack.index(x)))
            else:
                self.dfs(candidates, child, stack, result)
                candidates.append(stack.pop(stack.index(x)))


if __name__ == "__main__":
    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(Solution().combinationSum2([2, 5, 2, 1, 2], 5))
    print(Solution().combinationSum2([1, 2], 4))
    print(Solution().combinationSum2([1], 2))