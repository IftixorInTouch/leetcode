from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        zero_sequence = 0
        for num in nums:
            if num == 0:
                zero_sequence += 1
                result += zero_sequence
            else:
                zero_sequence = 0
        return result
