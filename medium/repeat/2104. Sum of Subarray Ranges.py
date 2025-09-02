from typing import List


class Solution:
    """
    Brute force algorithm
    """

    def subArrayRanges(self, nums: List[int]) -> int:
        result = 0

        for i in range(len(nums)):
            cur_max = nums[i]
            cur_min = nums[i]
            for j in range(i, len(nums)):
                if nums[j] > cur_max:
                    cur_max = nums[j]
                elif nums[j] < cur_min:
                    cur_min = nums[j]

                result += cur_max - cur_min
        return result


class Solution2:
    """
    Implement O(n) algorithm
    """
