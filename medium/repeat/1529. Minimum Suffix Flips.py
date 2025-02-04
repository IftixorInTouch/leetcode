#  Time limit exceeded
class Solution:
    """Time limit exceeded"""

    def minFlips(self, target: str) -> int:
        idx = len(target) - 2
        result = 0
        flag = 0
        target = list(target)
        while idx != -1:
            if target[idx] != target[idx + 1]:
                flag += 1
            if flag == 2:
                for i in range(idx + 1, len(target)):
                    target[i] = str(int(target[i]) ^ 1)
                flag = 0
                idx = len(target) - 2
                result += 1
                continue
            idx -= 1
        if flag == 0:
            return result
        if target[-1] == '1':
            return result + 1
        return result + 2
