from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = nums[0]

        for i in range(1, len(nums)):
            cur_sum = max(cur_sum + nums[i], nums[i])
            max_sum = max(cur_sum, max_sum)

        return max_sum


class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        """ Divide and conquer approach"""
        pass


a = Solution()
print(a.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
