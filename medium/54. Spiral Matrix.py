from typing import List

matrix = [[7],
          [9],
          [6]]


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top, bottom, left, right = 0, len(matrix), 0, len(matrix[0])
        while left < right and top < bottom:

            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                result.append(matrix[i][right - 1])

            right -= 1

            if bottom > top:
                for i in range(right - 1, left - 1, -1):
                    result.append(matrix[bottom - 1][i])

            bottom -= 1

            if right > left:
                for i in range(bottom - 1, top - 1, -1):
                    result.append(matrix[i][left])

            left += 1
        return result


a = Solution()
print(a.spiralOrder(matrix))
