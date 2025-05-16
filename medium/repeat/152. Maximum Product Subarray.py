from typing import List


class Solution:
    """Time limit exceeded."""

    def maxProduct(self, nums: List[int]) -> int:
        max_product = float("-inf")
        for i in range(len(nums)):
            cur_product = 1
            for j in range(i, len(nums)):
                cur_product *= nums[j]
                max_product = max(max_product, cur_product)
        return max_product
