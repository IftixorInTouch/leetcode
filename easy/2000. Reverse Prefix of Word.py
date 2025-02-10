class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        result = list(word)
        for i in range(len(result)):
            if result[i] == ch:
                left = 0
                right = i
                while left < right:
                    result[left], result[right] = result[right], result[left]
                    left += 1
                    right -= 1
                return "".join(result)
        return word
