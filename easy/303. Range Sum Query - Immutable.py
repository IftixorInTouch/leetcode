from typing import List

nums1 = [-2, 0, 3, -5, 2, -1]


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right + 1])


a = NumArray(nums1)
print(a.sumRange(0, 5))
