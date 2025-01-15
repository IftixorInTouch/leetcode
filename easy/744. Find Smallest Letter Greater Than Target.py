from typing import List

letters1 = ["c", "f", "j"]
letters2 = ["c", "f", "j"]
letters3 = ["x", "x", "y", "y"]


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if target < letter:
                return letter
        return letters[0]


a = Solution()
print(a.nextGreatestLetter(letters3, 'z'))
