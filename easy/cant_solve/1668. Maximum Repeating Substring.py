class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        left = 0
        right = len(word)
        result = 0
        while right != len(sequence)
            if sequence[left:right] == word:
                result += 1
                left = right
                right += len(word)
            left += 1
            right += 1
        return result


a = Solution()
print(a.maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba"))
