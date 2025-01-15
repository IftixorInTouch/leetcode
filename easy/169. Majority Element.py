from typing import List

nums1 = [3, 3, 4]
nums2 = [2, 2, 1, 1, 1, 2, 2]


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = {}
        for num in nums:
            if num in result:
                result[num] += 1
            else:
                result.update({num: 1})
        for key in result:
            if result[key] == max(result.values()):
                return key


class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]


class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


a = Solution()
print(a.majorityElement(nums1))
