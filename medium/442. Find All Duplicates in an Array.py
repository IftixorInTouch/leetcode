from typing import List

nums = [4, 3, 2, 7, 8, 2, 3, 1]


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                result.append(abs(num))
            nums[abs(num) - 1] *= -1
        return result


a = Solution()
print(a.findDuplicates(nums))
