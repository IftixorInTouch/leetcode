from typing import List

matrix = [[1, 1, 1], [1, 0, 0], [1, 1, 1]]


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if (matrix[row][col]) == 0:
                    rows.add(row)
                    cols.add(col)
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if row in rows or col in cols:
                    matrix[row][col] = 0


class Solution2:
    def make_zeros(self, matrix, i, j):
        for x in range(len(matrix[i])):
            if matrix[i][x] != 0:
                matrix[i][x] = '0'
        for y in range(len(matrix)):
            if matrix[y][j] != 0:
                matrix[y][j] = '0'

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    self.make_zeros(matrix, i, j)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '0':
                    matrix[i][j] = 0
        print(matrix)


a = Solution()
a.setZeroes(matrix)
