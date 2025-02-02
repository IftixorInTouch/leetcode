from typing import List


# not readable
class Solution:
    """not readable"""

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [f"{nums[0]}"]
        result = []
        left_index = 0
        previous = nums[0]
        for idx in range(1, len(nums)):
            if nums[idx] - previous != 1:
                if idx - left_index > 1:
                    result.append(f"{nums[left_index]}->{nums[idx - 1]}")
                else:
                    result.append(f"{nums[left_index]}")
                left_index = idx
            previous = nums[idx]
        if (len(nums) - 1) - left_index == 0:
            result.append(f"{nums[left_index]}")
        else:
            result.append(f"{nums[left_index]}->{nums[-1]}")
        return result


# good code
class Solution2:
    """good code"""

    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1

            if start == nums[i]:
                res.append(str(start))
            else:
                res.append(str(start) + "->" + str(nums[i]))
            i += 1

        return res
