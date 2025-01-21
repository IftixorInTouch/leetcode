from typing import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        result = 0
        nums.sort()
        max_num = nums[-1]
        len_nums = len(nums)
        for i in range(len_nums - 1, -1, -1):
            if nums[i] != max_num:
                result += len_nums - i - 1
                max_num = nums[i]

        return result


a = Solution()
print(a.reductionOperations([1, 1, 2, 2, 3]))
