from collections import Counter
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d = Counter(nums)
        result = []
        result_len = d.most_common()[0][1]
        for i in range(result_len):
            result.append([])

        for num in nums:
            result[d[num] - 1].append(num)
            d[num] -= 1
        return result

a = Solution()
print(a.findMatrix([1,3,4,1,2,3,1]))
