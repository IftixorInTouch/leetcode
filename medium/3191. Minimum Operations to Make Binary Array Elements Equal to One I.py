from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result = 0
        for idx, num in enumerate(nums):
            print(nums)
            if num == 0 and len(nums[idx:]) >= 3:
                result += 1
                nums[idx] ^= 1
                nums[idx + 1] ^= 1
                nums[idx + 2] ^= 1
        if nums.count(1) == len(nums):
            return result
        return -1


nums = [1, 0, 1, 1, 0, 0, 1]
a = Solution()
print(a.minOperations(nums))
