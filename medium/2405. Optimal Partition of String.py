class Solution:
    def partitionString(self, s: str) -> int:
        result = 0
        sub_s = ""
        for char in s:
            if char in sub_s:
                result += 1
                sub_s = char
            else:
                sub_s += char
        return result + 1
