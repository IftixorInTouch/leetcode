from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        height = len(mat)
        width = len(mat[0])
        i = 0
        j = 0
        result = []
        for _ in range(height * width):
            result.append(mat[i][j])
            if (i + j) % 2 == 0:
                if j == width - 1:
                    i += 1
                elif i == 0:
                    j += 1
                else:
                    i -= 1
                    j += 1
            else:
                if i == height - 1:
                    j += 1
                elif j == 0:
                    i += 1
                else:
                    i += 1
                    j -= 1
        return result


a = Solution()
print(a.findDiagonalOrder([[1, 2], [3, 4]]))
