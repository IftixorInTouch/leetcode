from typing import List


class Solution:
    """Brute force solution"""

    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        result = []
        for idx1, n1 in enumerate(nums1):
            for idx2, n2 in enumerate(nums2):
                if n1 <= n2 and idx1 <= idx2:
                    result.append(idx2 - idx1)
        return max(result)


class Solution2:

    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        idx1, idx2 = 0, 0

        while idx1 < len(nums1) and idx2 < len(nums2):
            if idx1 == idx2 and nums1[idx1] > nums2[idx2]:
                idx1 += 1
                idx2 += 1
            elif nums1[idx1] > nums2[idx2]:
                idx1 += 1
            elif idx1 <= idx2 and nums1[idx1] <= nums2[idx2]:
                result = max(idx2 - idx1, result)
                idx2 += 1
        return result


a = Solution2()
print(a.maxDistance([55,30,5,4,2], [100,20,10,10,5]))
