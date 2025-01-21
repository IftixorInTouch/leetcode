from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        if time == 0:
            return [i for i in range(len(security))]

        decreasing = [0] * len(security)
        increasing = [0] * len(security)
        result = []
        for i in range(1, len(security)):
            if security[i] <= security[i - 1]:
                decreasing[i] = decreasing[i - 1] + 1

        for i in range(len(security) - 2, -1, -1):
            if security[i] <= security[i + 1]:
                increasing[i] = increasing[i + 1] + 1

        for idx, (i, j) in enumerate(zip(decreasing, increasing)):
            if i >= time and j >= time:
                result.append(idx)

        return result

a = Solution()
print(a.goodDaysToRobBank([5,3,3,3,5,6,2], 2))