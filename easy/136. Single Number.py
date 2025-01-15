from typing import List

nums1 = [2, 2, 1]
nums2 = [4, 1, 2, 1, 2]
nums3 = [1]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = sum(set(nums)) - (sum(nums) / 2)
        return int((s * 2))


a = Solution()
print(a.singleNumber(nums3))
