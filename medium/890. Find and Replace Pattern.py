from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        for word in words:
            first_bijection = {}
            second_bijection = {}
            valid = False
            for pattern_letter, word_letter in zip(pattern, word):
                first_bijection.update({pattern_letter: word_letter})
                second_bijection.update({word_letter: pattern_letter})

            for pattern_letter, word_letter in zip(pattern, word):
                if first_bijection[pattern_letter] != word_letter:
                    valid = False
                    break
                if second_bijection[word_letter] != pattern_letter:
                    valid = False
                    break
                valid = True
            if valid:
                result.append(word)
        return result


a = Solution()
print(a.findAndReplacePattern(["a","b","c"], "a"))
