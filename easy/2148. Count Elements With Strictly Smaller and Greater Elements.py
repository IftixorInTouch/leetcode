from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)

        return sum(1 for num in nums if min_num < num < max_num)
