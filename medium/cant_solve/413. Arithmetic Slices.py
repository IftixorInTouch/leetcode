from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        result = 0
        left_num = nums[0]
        diff = nums[1] - left_num
        len_of_subarray = 1
        sub_array = nums[:3]
        while len(sub_array) >= 3:


[1,2,3,4,7,9,11]
a = Solution()
print(a.numberOfArithmeticSlices([2,1,3,4,2,3]))


# class Solution:
#     def numberOfArithmeticSlices(self, nums: List[int]) -> int:
#         if len(nums) < 3:
#             return 0
#
#         def valid_subarray(array):
#             left_num = array[0]
#             diff = array[1] - left_num
#             for num in array[1:]:
#                 if diff != num - left_num:
#                     return False
#                 diff = num - left_num
#                 left_num = num
#             return True
#
#         left = right = result = 0
#         while right < len(nums):
