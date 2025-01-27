from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        left = min(a, b, c)
        right = max(a, b, c)
        middle = 0
        if a in range(left + 1, right):
            middle = a
        elif b in range(left + 1, right):
            middle = b
        else:
            middle = c

        result = [0, 0]

        if abs(middle - left) > 1:
            result[0] += 1
        if abs(middle - right) > 1:
            result[0] += 1

        if abs(middle - left) == 2 or abs(middle - right) == 2:
            result[0] = 1

        result[1] = abs(middle - left) + abs(middle - right) - 2
        return result

a = Solution()
print(a.numMovesStones(1, 2, 5))