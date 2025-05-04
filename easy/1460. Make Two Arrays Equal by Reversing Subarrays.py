from collections import Counter, defaultdict
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if Counter(target) == Counter(arr):
            return True
        return False


class Solution2:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        dict_1 = defaultdict(int)
        dict_2 = defaultdict(int)
        for i, j in zip(target, arr):
            dict_1[i] += 1
            dict_2[j] += 1

        return dict_1 == dict_2
