from typing import List


class Solution:
    """
    Time limit exceeded
    """

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        pos_nums = []
        result = 0
        for idx, num in enumerate(nums):
            if num < k:
                result += 1
                pos_nums.append((idx, num))

        for idx, num in enumerate(nums):
            iter_pos_nums = pos_nums.copy()
            for t in iter_pos_nums:
                if idx - t[0] == 1:
                    if num * t[1] < k:
                        result += 1
                        pos_nums.append((idx, num * t[1]))

        return result


class Solution2:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        result = 0
        cur_product = 1
        for right in range(len(nums)):
            cur_product *= nums[right]

            while cur_product >= k and left <= right:
                cur_product //= nums[left]
                left += 1

            result += right - left + 1

        return result


a = Solution2()
print(a.numSubarrayProductLessThanK([1, 2, 3, 4], 2))
