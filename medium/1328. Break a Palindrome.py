class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""

        left = 0
        right = len(palindrome) - 1
        palindrome_lst = list(palindrome)
        while left < right:
            if palindrome_lst[left] != 'a':
                palindrome_lst[left] = 'a'
                return ''.join(palindrome_lst)
            left += 1
            right -= 1

        palindrome_lst[-1] = 'b'
        return ''.join(palindrome_lst)


a = Solution()
print(a.breakPalindrome("aba"))
