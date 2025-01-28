# not optimal
class Solution:
    """Not optimal"""

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        for idx in range(len(s2) - (len(s1) - 1)):
            tmp_s = sorted(s2[idx:idx + len(s1)])
            if s1 == tmp_s:
                return True
        return False
