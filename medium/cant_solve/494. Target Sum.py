from typing import List


# class IncorrectSolution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         def find_target_sum(nums, target):
#             nums_sum = sum(nums)
#             for i in range(len(nums) - 1, -1, -1):
#                 if nums_sum == target:
#                     return nums
#                 if nums_sum - (2 * nums[i]) < target:
#                     continue
#                 nums_sum -= 2 * nums[i]
#                 nums[i] = -nums[i]
#             return 0
#
#         nums.sort()
#         result_nums = []
#
#         correct_nums = find_target_sum(nums, target)
#         print(correct_nums)
#         if correct_nums not in result_nums and correct_nums != 0:
#             result_nums.append(correct_nums)
#         for i in range(len(nums)):
#             nums = list(map(lambda x: abs(x), nums))
#             nums[i] = -nums[i]
#             correct_nums = find_target_sum(nums, target)
#             if correct_nums not in result_nums and correct_nums != 0:
#                 result_nums.append(correct_nums)
#         print(result_nums)
#         return len(result_nums)
class VerySlowSolution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mask = []

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
        result = 0
        for sub_mask in mask:
            nums = list(map(lambda x: abs(x), nums))
            for idx, bit in enumerate(sub_mask):
                if bit == 1:
                    nums[idx] = -nums[idx]
            if sum(nums) == target:
                result += 1
        return result


a = Solution()
print(a.findTargetSumWays([42,24,30,14,38,27,12,29,43,42,5,18,0,1,12,44,45,50,21,47], 38))
