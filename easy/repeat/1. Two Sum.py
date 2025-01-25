from typing import List

nums1 = [2, 7, 11, 15]
nums2 = [3, 2, 4]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            minus = nums[i] - target
            if minus in nums[i:]:
                return True
            # for j in range(i + 1, len(nums)):
            #     if (nums[i] + nums[j]) == target:
            #         return [i, j]


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}

        for i in range(len(nums)):

            if target - nums[i] in memo:
                return [memo[target - nums[i]], i]
            memo[nums[i]] = i

        return []


a = Solution()
print(a.twoSum(nums1, 6))
