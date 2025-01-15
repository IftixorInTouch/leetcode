from typing import List

original = [1, 2, 1, 6]
m = 2
n = 2


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        length = len(original)
        if length != n * m:
            return []
        result = []
        for i in range(0, length, n):
            result.append(original[i: i + n])
        return result


a = Solution()
print(a.construct2DArray(original, m, n))
