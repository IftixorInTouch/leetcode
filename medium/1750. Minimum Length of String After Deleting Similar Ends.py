class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) < 3:
            return len(s)
        deleted_chars = 0
        prefix = 0
        suffix = len(s) - 1
        tmp_char = s[0]
        while s[prefix] == s[suffix] and prefix < suffix:
            while prefix < len(s) and s[prefix] == tmp_char:
                prefix += 1
                deleted_chars += 1
            while suffix > -1 and s[suffix] == tmp_char:
                suffix -= 1
                deleted_chars += 1
            if prefix >= len(s):
                break
            tmp_char = s[prefix]
        if deleted_chars >= len(s):
            return 0
        return len(s) - deleted_chars
