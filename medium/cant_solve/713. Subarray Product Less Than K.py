from typing import List


class Solution:
    """
    Time limit exceeded
    """

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        pos_nums = []
        result = 0
        for idx, num in enumerate(nums):
            if num < k:
                result += 1
                pos_nums.append((idx, num))

        for idx, num in enumerate(nums):
            iter_pos_nums = pos_nums.copy()
            for t in iter_pos_nums:
                if idx - t[0] == 1:
                    if num * t[1] < k:
                        result += 1
                        pos_nums.append((idx, num * t[1]))

        return result
