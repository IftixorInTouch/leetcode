from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefix_sum = 0
        sums_dict = {0: 1}
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in sums_dict:
                result += sums_dict[prefix_sum - k]
            sums_dict[prefix_sum] = 1 + sums_dict.get(prefix_sum, 0)
        return result


a = Solution()
print(a.subarraySum([1], 0))
