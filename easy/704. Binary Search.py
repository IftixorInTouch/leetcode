from typing import List

nums = [-1, 0, 3, 5, 6, 9, 12, 15, 17, 18]
target = -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            idx = int((left + right) / 2)
            if nums[idx] < target:
                left = idx + 1
            elif nums[idx] > target:
                right = idx - 1
            else:
                return idx
        return -1


a = Solution()
print(a.search(nums, target))
