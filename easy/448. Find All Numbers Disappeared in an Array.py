from typing import List

nums1 = [1, 1]
nums2 = [4, 3, 2, 7, 8, 2, 3, 1, 9]


# [0, 1, 2, 3, 4, 5, 6, 7, 8]
# [3, 2, 3, 4, 8, 2, 7, 1, 9]

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))


class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        result = []
        while i < len(nums):
            pos = nums[i] - 1
            if nums[i] != nums[pos]:
                nums[i], nums[pos] = nums[pos], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                result.append(i + 1)
        return result


a = Solution2()
print(a.findDisappearedNumbers(nums2))
