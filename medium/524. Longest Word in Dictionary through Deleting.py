from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        result = ""
        for word in dictionary:
            s_iter = 0
            word_iter = 0
            while s_iter < len(s):
                if word_iter == len(word):
                    if len(result) < len(word):
                        result = word
                    elif len(result) == len(word):
                        if word < result:
                            result = word
                    break
                if s[s_iter] == word[word_iter]:
                    s_iter += 1
                    word_iter += 1
                else:
                    s_iter += 1
            if word_iter == len(word):
                if len(result) < len(word):
                    result = word
                elif len(result) == len(word):
                    if word < result:
                        result = word
        return result


print("abe" < "abc")
a = Solution()
print(a.findLongestWord("aaa", ["aaa", "aa", "a"]))


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary = sorted(dictionary, key=lambda x: (-len(x), x))

        def valid(word: str, s: str) -> bool:
            left, right = 0, 0
            while left < len(s) and right < len(word):
                if s[left] == word[right]:
                    right += 1
                left += 1
            return right == len(word)

        for word in dictionary:
            if valid(word, s):
                return word

        return ""
