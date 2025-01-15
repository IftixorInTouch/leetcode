from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost1 = cost[0]
        cost2 = cost[1]
        for i in cost[2:]:
            tmp_cost = i + min(cost1, cost2)
            cost1 = cost2
            cost2 = tmp_cost
        return min(cost1, cost2)


a = Solution()
print(a.minCostClimbingStairs([10, 1, 20, 10, 1, 15, 15, 1]))
