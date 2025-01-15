from collections import defaultdict, Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s) == 1:
            return s
        s = list(s)
        char_dict = Counter(s)
        most_common = char_dict.most_common()
        if most_common[0][-1] > (len(s) + 1) // 2:
            return ""
        result_s = [""] * len(s)
        i = 0
        for key, freq in most_common:
            for j in range(freq):
                if i >= len(s):
                    i = 1
                result_s[i] = key
                i += 2
        return "".join(result_s)


a = Solution()
print(a.reorganizeString("vvvlo"))
