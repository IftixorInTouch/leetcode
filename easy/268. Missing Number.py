from typing import List

nums1 = [3, 0, 1]
nums2 = [0, 1]
nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        s = int((n - 1) / 2 * n)
        for num in nums:
            s -= num
        return s


a = Solution()
print(a.missingNumber(nums3))
