from collections import deque
from typing import List

nums = [-4, -1, 0, 3, 10]


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] **= 2
        nums.sort()
        return nums


class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = deque()
        start = 0
        end = len(nums) - 1
        while start <= end:
            start_sq = nums[start] ** 2
            end_sq = nums[end] ** 2
            if start_sq > end_sq:
                result.appendleft(start_sq)
                start += 1
            else:
                result.appendleft(end_sq)
                end -= 1
        return list(result)


a = Solution2()
print(a.sortedSquares(nums))
