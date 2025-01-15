from typing import List

nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 3, 4]
nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]


# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         first = nums[0]
#         for num in nums[1:]:
#             if first == num:
#                 return True
#             first = num
#         return False
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for num in nums:
            if my_dict.get(num) is None:
                my_dict.update({num: 1})
            else:
                return True
        return False

b = {1, 2, 3, 4, 1}
print(b)
# a = Solution()
# print(a.containsDuplicate(nums1))
