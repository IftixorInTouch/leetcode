from typing import List


class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        result = 0
        maximum_num = -10 ** 6
        for i in range(4):
            idx = 0
            for num in b[idx:]:
                if a[i] * num > maximum_num:


a = Solution()
print(a.maxScore([3, 2, 5, 6], [2, -6, 4, -5, -3, 2, -7]))
