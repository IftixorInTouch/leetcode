from typing import List

nums1 = [1, 1]
nums2 = [4, 3, 2, 7, 8, 2, 3, 1, 9]


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        full_lst = list(range(1, len(nums) + 1))
        full_lst = set(full_lst)
        nums = set(nums)
        full_lst -= nums
        return list(full_lst)


a = Solution()
print(a.findDisappearedNumbers(nums2))
