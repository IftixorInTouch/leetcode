from typing import List


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        return int(((max_num + (max_num + k - 1)) / 2) * k)
