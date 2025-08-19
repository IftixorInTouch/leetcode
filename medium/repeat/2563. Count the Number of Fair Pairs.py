from typing import List


# brute force, time limit exceeded
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i < j and lower <= nums[i] + nums[j] <= upper:
                    result += 1
                    nums = set(nums)
                    
        return result
