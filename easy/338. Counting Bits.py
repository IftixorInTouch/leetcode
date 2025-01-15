from typing import List


class Solution1:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(0, n + 1):
            answer.append(i.bit_count())
        return answer


class Solution2:

    def ten_to_two(self, n):
        answer = []
        while n != 0:
            answer.append(n % 2)
            n = int(n / 2)
        return answer

    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(0, n + 1):
            answer.append(sum(self.ten_to_two(i)))
        return answer


a = Solution1()
print(a.countBits(5))
