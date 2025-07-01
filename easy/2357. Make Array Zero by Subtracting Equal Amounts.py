from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = set(nums).difference({0})
        return len(nums)
