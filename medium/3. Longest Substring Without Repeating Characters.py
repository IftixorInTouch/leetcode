class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            current_max_substring = 0
            substring = {}
            end = 0
            for char in s[i:]:
                if char not in substring:
                    substring.update({char: 1})
                    current_max_substring += 1
                else:
                    break
                end += 1
            if current_max_substring > result:
                result = current_max_substring
            if end == len(s[i:]):
                break
        return result


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        cur_max = 0
        sub_string = ""
        for char in s:
            if char not in sub_string:
                sub_string += char
            else:
                for i in range(len(sub_string)):
                    if sub_string[i] == char:
                        sub_string = sub_string[i + 1:]
                        break
                sub_string += char
            cur_max = len(sub_string)
            if cur_max > result:
                result = cur_max
        return result


class LeetCodeSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_length = 0
        char_set = set()

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length


a = Solution()
print(a.lengthOfLongestSubstring("abbaaabcd"))

b = Solution2()
print(b.lengthOfLongestSubstring("abbaaabcd"))
