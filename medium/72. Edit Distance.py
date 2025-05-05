class Solution:
    """Time limit exceeded."""

    def minDistance(self, word1: str, word2: str) -> int:
        def lev(word1, word2):
            if len(word1) == 0:
                return len(word2)
            if len(word2) == 0:
                return len(word1)
            if word1[0] == word2[0]:
                return lev(word1[1:], word2[1:])
            return 1 + min(
                lev(word1, word2[1:]),
                lev(word1[1:], word2),
                lev(word1[1:], word2[1:])
            )

        return lev(word1, word2)


class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + 1
        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] + 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[n][m]


a = Solution2()
print(a.minDistance("ab", "cdasdf"))
