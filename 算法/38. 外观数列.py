class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        elif n == 3:
            return "21"
        else:
            result = ""
            prev = self.countAndSay(n - 1)
            stack = [prev[0]]
            for x in prev[1:]:
                if x == stack[-1]:
                    stack.append(x)
                else:
                    result = result + str(len(stack)) + str(stack[0])
                    stack.clear()
                    stack.append(x)
            result = result + str(len(stack)) + str(stack[0])
            stack.clear()
            return result


if __name__ == "__main__":
    print(Solution().countAndSay(3))
    print(Solution().countAndSay(5))