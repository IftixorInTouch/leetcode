class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        space_counter = 0
        for idx, char in enumerate(s):
            if char == ' ':
                space_counter += 1
            if space_counter == k:
                return s[:idx]
        return s
