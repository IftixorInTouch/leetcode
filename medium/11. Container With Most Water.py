from typing import List


class Solution:
    """
    Not optimal
    Time complexity: O(n^2)
    """

    def maxArea(self, height: List[int]) -> int:
        result = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                result = max(result, (j - i) * min(height[i], height[j]))
        return result


class Solution2:
    """
    Optimal solution
    Time complexity: O(n)
    """

    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        result = 0
        while left < right:
            result = max(result, (right - left) * min(height[left], height[right]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return result


a = Solution2()
print(a.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
