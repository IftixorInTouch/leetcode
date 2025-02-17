from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = 0
        cur_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur_sum += nums[i]
            else:
                if cur_sum > result:
                    result = cur_sum
                cur_sum = nums[i]
        if cur_sum > result:
            result = cur_sum
        return result
