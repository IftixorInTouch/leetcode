from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            for s in str(num):
                result.append(int(s))
        return result


a = Solution()
print(a.separateDigits([13, 25, 83, 77]))
