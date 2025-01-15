from collections import defaultdict
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        sum_dict = defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                sum_dict[i + j].append([i, j])
        result = []
        for lst in sum_dict.values():
            for inner_lst in lst[::-1]:
                result.append(nums[inner_lst[0]][inner_lst[1]])
        return result


a = Solution()
print(a.findDiagonalOrder([[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]))
