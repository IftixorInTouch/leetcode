from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        result = float('inf')
        for i in range(len(nums) // 2):
            if result > ((nums[i] + nums[~i]) / 2):
                result = (nums[i] + nums[~i]) / 2
        return result
