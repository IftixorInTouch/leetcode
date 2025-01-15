import math
from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = [0] * len(nums)
        left = 0
        mid = math.ceil(len(nums) / 2)
        for i in range(len(nums)):
            if i % 2 == 0:
                result[i] = nums[left]
                left += 1
            else:
                result[i] = nums[mid]
                mid += 1
        return result
