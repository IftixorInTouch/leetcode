s = "ab"
t = "baab"


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i = 0
        for letter in t:
            if i < len(s) and letter == s[i]:
                i += 1
            else:
                t = t.replace(letter, '', 1)
        return s == t


class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


a = Solution()
print(a.isSubsequence(s, t))

