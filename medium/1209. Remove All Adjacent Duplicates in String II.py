class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if stack and stack[-1][0] + 1 == k and stack[-1][1] == char:
                stack.pop()
            elif stack and stack[-1][1] == char:
                stack[-1][0] += 1
            else:
                stack.append([1, char])
        result = []
        for elem in stack:
            result.append(elem[1] * elem[0])
        return "".join(result)
