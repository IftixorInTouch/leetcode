from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dct = {}
        result = 0
        for idx, num in enumerate(nums):
            str_num = str(num)
            digits_sum = 0
            for digit in str_num:
                digits_sum += int(digit)

            tmp = dct.get(digits_sum)

            if tmp is not None:
                if nums[tmp] + num > result:
                    result = nums[tmp] + num
                if nums[tmp] < num:
                    dct[digits_sum] = idx
            else:
                dct[digits_sum] = idx
        if result == 0:
            return -1
        return result


a = Solution()
print(a.maximumSum([18,43,36,13]))
