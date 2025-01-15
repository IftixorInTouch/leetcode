class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        tn = 0
        t1, t2, t3 = 0, 1, 1
        if n == 1:
            return t2
        if n == 2:
            return t3
        for i in range(n - 2):
            tn = t1 + t2 + t3
            t1, t2, t3 = t2, t3, tn
        return tn


a = Solution()
print(a.tribonacci(5))
