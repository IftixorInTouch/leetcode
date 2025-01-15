class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        result = 0
        first_word = word
        while word in sequence:
            result += 1
            word = first_word + word
        return result
