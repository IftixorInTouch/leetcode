class Solution:
    def numSub(self, s: str) -> int:
        result = 0
        substring_len = 0
        for char in s:
            if char == "1":
                substring_len += 1
                result += substring_len
            else:
                substring_len = 0
        return result % (10 ** 9 + 7)
