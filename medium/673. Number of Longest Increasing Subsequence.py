from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        result = 0
        helper = [[nums[0]]]
        for num in nums:
            print(helper)
            for help in helper:
                print(help)
                if help[-1] < num:
                    helper.append(help + [num])

        max_length = max(len(help) for help in  helper)
        for help in helper:
            if len(help) == max_length:
                result += 1

        return result

a = Solution()
print(a.findNumberOfLIS([1, 1, 2, 2, 3, 3]))
