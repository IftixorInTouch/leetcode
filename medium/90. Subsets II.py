from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        mask = []
        nums.sort()

        def ten_to_binary(num):
            binary = [0] * len(nums)
            idx = 0
            while num != 0:
                binary[idx] = (num % 2)
                num = num // 2
                idx += 1
            return binary

        def define_mask():
            for i in range(2 ** len(nums)):
                mask.append(ten_to_binary(i))

        define_mask()
        for sub_mask in mask:
            sub_result = []
            for idx, bit in enumerate(sub_mask):
                if bit == 1:
                    sub_result.append(nums[idx])
            if sub_result not in result:
                result.append(sub_result)
        return result


a = Solution()
print(a.subsetsWithDup([4, 4, 4, 1, 4]))
