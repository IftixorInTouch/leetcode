class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence_list = sentence.split(" ")
        for i, word in enumerate(sentence_list):
            if word[:len(searchWord)] == searchWord:
                return i + 1
        return -1


a = Solution()
print(a.isPrefixOfWord("i am tired", "you"))
