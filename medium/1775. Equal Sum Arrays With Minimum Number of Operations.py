from collections import defaultdict
from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        if sum2 > sum1:
            nums1, nums2 = nums2, nums1
            sum1 = sum(nums1)
            sum2 = sum(nums2)

        nums1_dict = defaultdict(int)
        nums2_dict = defaultdict(int)
        for num in nums1:
            nums1_dict[num] += 1
        for num in nums2:
            nums2_dict[num] += 1

        while sum2 < sum1:
            max1 = max(nums1_dict)
            min2 = min(nums2_dict)
            if max1 == 1 and min2 == 6:
                return -1
            tmp1 = max1 - 1
            tmp2 = 6 - min2

            if tmp1 >= tmp2:
                sum1 -= tmp1
                nums1_dict[max1] -= 1
                nums1_dict[1] += 1
                if nums1_dict[max1] == 0:
                    nums1_dict.pop(max1)
            elif tmp2 > tmp1:
                sum2 += tmp2
                nums2_dict[min2] -= 1
                nums2_dict[6] += 1
                if nums2_dict[min2] == 0:
                    nums2_dict.pop(min2)

            result += 1
        return result


a = Solution()
print(a.minOperations([5, 2, 1, 5, 2, 2, 2, 2, 4, 3, 3, 5], [1, 4, 5, 5, 6, 3, 1, 3, 3]))
