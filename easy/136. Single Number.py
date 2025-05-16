from typing import List

nums1 = [2, 2, 1]
nums2 = [4, 1, 2, 1, 2]
nums3 = [1]


class Solution:
    """
    Time: O(n)
    Space: O(n)    -   converting to set takes space
    """
    def singleNumber(self, nums: List[int]) -> int:
        """
        s_dupl = sum(set(nums))

        s_1 = s_dupl + x
        s_2 = 2 * s_dupl + x

        We have system of linear equations. We need to find the x.
        x = 2 * s_dupl - sum(nums)
        :param nums:
        :return:
        """
        return 2 * sum(set(nums)) - sum(nums)

class Solution2:
    """
    Solving using XOR
    """

    def singleNumber(self, nums: List[int]) -> int:
        mask = 0
        for num in nums:
            mask ^= num
        return mask

a = Solution()
print(a.singleNumber(nums3))
