class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        """
        :type purchaseAmount: int
        :rtype: int
        """
        if purchaseAmount % 10 < 5:
            purchaseAmount = purchaseAmount // 10
            purchaseAmount *= 10
            return 100 - int(purchaseAmount)
        else:
            purchaseAmount = purchaseAmount // 10
            purchaseAmount = purchaseAmount * 10 + 10
            return 100 - int(purchaseAmount)

a = Solution()
print(a.accountBalanceAfterPurchase(11))