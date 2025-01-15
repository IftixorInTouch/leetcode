from typing import List

prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]
prices3 = [2, 6, 1, 3, 3]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell > buy:
                profit = max(sell - buy, profit)
            else:
                buy = sell
        return profit


a = Solution()
print(a.maxProfit(prices3))
