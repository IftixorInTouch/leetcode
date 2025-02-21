class Solution:
    def minOperations(self, n: int) -> int:
        return int(((n % 2) + n) / 2 * (n // 2))


#  not optimized
class Solution2:
    """not optimized"""

    def minOperations(self, n: int) -> int:
        result = 0
        for i in range(n // 2):
            result += n - (2 * i + 1)
        return result
