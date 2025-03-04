from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        result = float('inf')
        for num in nums:
            abs_result = abs(result)
            if abs(num) < abs_result:
                result = num
            elif abs_result == num:
                result = num
        return result
