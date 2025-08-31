class Solution:
    """
    Brute force algorithm
    Time Limit Exceeded
    """

    def longestPalindrome(self, s: str) -> str:
        result = []
        for i in range(len(s)):
            sub_s = []
            for j in range(i, len(s)):
                sub_s.append(s[j])
                if self.is_palindrome(sub_s) and len(result) < len(sub_s):
                    result = sub_s.copy()
        return "".join(result)

    def is_palindrome(self, s):
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


class Solution2:
    """
    Center expansion algorithm
    """

    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        max_str = s[0]

        for i in range(len(s) - 1):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str


class Solution3:
    """
    Manacher's Algorithm
    """

    def longestPalindrome(self, s: str) -> str:
        pass


class Solution4:
    """
    DP Algorithm
    """

    def longestPalindrome(self, s: str) -> str:
        pass
