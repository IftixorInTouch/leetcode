from typing import List


class Solution:
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y
    }

    def diffWaysToCompute(self, expression: str) -> List[int]:
        result = []
        for i in range(len(expression)):
            if expression[i] in self.operations:
                op = expression[i]
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                for n1 in left:
                    for n2 in right:
                        result.append(self.operations[op](n1, n2))
        if not result:
            result.append(int(expression))
        return result

class Solution2:
    """
    Implement solution with memoization using dynamic programming approach.
    """

a = Solution()
print(a.diffWaysToCompute("1+2+3"))
