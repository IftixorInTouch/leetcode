from collections import Counter
from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        if len(nums) != n + 1:
            return False

        count = Counter(nums)

        for i in range(1, n):
            if count[i] != 1:
                return False

        return count[n] == 2
