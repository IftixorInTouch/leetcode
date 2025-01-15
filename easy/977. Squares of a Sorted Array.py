from typing import List

nums = [-4, -1, 0, 3, 10]


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] **= 2
        nums.sort()
        return nums


a = Solution()
print(a.sortedSquares(nums))
