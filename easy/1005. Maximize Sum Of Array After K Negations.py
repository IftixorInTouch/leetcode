from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums[:k])):
            if nums[i] <= 0:
                nums[i] = abs(nums[i])
                k -= 1
        if k % 2 == 0:
            return sum(nums)
        else:
            return sum(nums) - (2 * min(nums))

