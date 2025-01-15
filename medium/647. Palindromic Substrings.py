# O(n^2)
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.result = 0

        def palindrome(s, left, right):
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                self.result += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            palindrome(s, i, i)
            palindrome(s, i, i + 1)

        return self.result

a = Solution()
print(a.countSubstrings("abba"))

# O(n^3)
class Solution2(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        def palindrome(substring):
            return substring == substring[::-1]

        for i in range(len(s)):
            substring = []
            for char in s[i:]:
                substring.append(char)
                if palindrome(substring):
                    result += 1
        return result