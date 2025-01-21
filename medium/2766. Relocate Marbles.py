from typing import List


class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        nums = set(nums)
        for pos1, pos2 in zip(moveFrom, moveTo):
            nums.remove(pos1)
            nums.add(pos2)

        sorted_nums_lst = sorted(nums)
        return sorted_nums_lst
