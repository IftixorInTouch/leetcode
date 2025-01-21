from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        stack = []

        for idx, num in enumerate(nums):
            while len(stack) != 0 and num > stack[-1][1]:
                result[stack[-1][0]] = num
                stack.pop()
            stack.append((idx, num))

        max_num = 0
        if len(stack) != 0:
            result[stack[0][0]] = -1
            max_num = stack[0][1]

        for idx, num in stack[1:]:
            if num < max_num:
                result[idx] = max_num
            else:
                result[idx] = -1

        return result