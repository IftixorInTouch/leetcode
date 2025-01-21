from typing import List


# brute force
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        self.result = []

        def ten_to_bin(num):
            bin_num = [0] * len(s)
            pos = 0

            while num != 0:
                bin_num[pos] = num % 2
                num = num // 2
                pos += 1

            new_s = ""
            for i in range(len(s)):
                if bin_num[i] == 1 and isinstance(s[i], str):
                    new_s += s[i].upper()
                elif bin_num[i] == 0 and isinstance(s[i], str):
                    new_s += s[i].lower()

            if new_s not in self.result:
                self.result.append(new_s)

        for i in range(2 ** len(s)):
            ten_to_bin(i)

        return self.result


# time limit exceeded
class Solution2:

    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        num_of_chars = 0
        for char in s:
            if char.isalpha():
                num_of_chars += 1

        for i in range(2 ** num_of_chars):
            sub_s = ""
            pos = 0
            for j in range(len(s)):
                sub_s += s[j]
                pos += 1
                if s[j].isalpha():
                    break

            s = s[pos:]
            if len(result) == 0:
                result.append(sub_s.lower())
                if sub_s.upper() not in result:
                    result.append(sub_s.upper())
                continue

            for k in range(len(result)):
                tmp_s = result[k]
                result[k] += sub_s.lower()
                new_s = tmp_s + sub_s.upper()
                if new_s not in result:
                    result.append(new_s)
        return result


# optimized
class Solution3:
    def letterCasePermutation(self, s: str) -> List[str]:
        self.s_len = len(s)
        self.result = []
        self.helper("", s)
        return self.result

    def helper(self, sub_s, s):
        if len(sub_s) == self.s_len:
            if sub_s not in self.result:
                self.result.append(sub_s)
            return

        tmp_s = ""
        for i in range(len(s)):
            tmp_s += s[i]
            if s[i].isalpha():
                s = s[i + 1:]
                break
        sub_s_1 = sub_s + tmp_s.lower()
        sub_s_2 = sub_s + tmp_s.upper()
        self.helper(sub_s_1, s)
        self.helper(sub_s_2, s)

# optimized
class Solution4:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = ['']

        for char in s:
            tmp_res = []
            for elem in result:
                if char.isalpha():
                    tmp_res.append(elem + char.lower())
                    tmp_res.append(elem + char.upper())
                else:
                    tmp_res.append(elem + char)
            result = tmp_res
        return result


# a = Solution4()
# print(a.letterCasePermutation("a1b2"))
# print(a.letterCasePermutation("3z4"))
# print(a.letterCasePermutation("12345"))
# print(a.letterCasePermutation("JcTNPT1AsvC"))
