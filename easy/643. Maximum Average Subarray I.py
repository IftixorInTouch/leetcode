from typing import List

nums = [10, 3, 2, -5, 6, -9]
k = 3


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        length = len(nums)
        i = 0
        max_average = sum(nums[:k])
        average = max_average
        while length - k > i:
            average = average - nums[i] + nums[i + k]
            if average > max_average:
                max_average = average
            i += 1
        return max_average / k


a = Solution()
print(a.findMaxAverage(nums, k))
