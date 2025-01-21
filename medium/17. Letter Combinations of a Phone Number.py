from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        self.result = []
        self.len_digits = len(digits)
        self.num_dict = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        self.helper("")

    def helper(self, word):
        if len(word) == self.len_digits:
            self.result.append(word)
            return


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        self.result = []
        self.digits = digits
        self.num_dict = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        self.backtrack(0, "")
        return self.result

    def backtrack(self, digit, string):
        if len(string) == len(self.digits):
            self.result.append(string)
            return
        next_letters = self.num_dict[int(self.digits[digit])]
        for letter in next_letters:
            self.backtrack(digit + 1, string + letter)

a= Solution()
print(a.letterCombinations("23"))