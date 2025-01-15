s = "ab#c"
t = "ad#c"


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        new_s = ''
        new_t = ''
        for char in s:
            if char == '#':
                new_s = new_s[:len(new_s) - 1]
            else:
                new_s += char
        for char in t:
            if char == '#':
                new_t = new_t[:len(new_t) - 1]
            else:
                new_t += char
        return new_s == new_t


a = Solution()
print(a.backspaceCompare(s, t))
