from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        flip_rows = 0
        flip_columns = 0

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            start = 0
            end = len(grid[0]) - 1
            while start < end:
                if grid[i][start] != grid[i][end]:
                    flip_rows += 1
                start += 1
                end -= 1

        for j in range(n):
            start = 0
            end = len(grid) - 1
            while start < end:
                if grid[start][j] != grid[end][j]:
                    flip_columns += 1
                start += 1
                end -= 1
        return min(flip_rows, flip_columns)


a = Solution()
print(a.minFlips([[1, 0, 0],
                  [0, 0, 0],
                  [0, 0, 1]]))
