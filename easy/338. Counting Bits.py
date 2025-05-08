import math
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


class Solution3:
    def countBits(self, n: int) -> List[int]:
        i = 1
        result = [0]
        while i <= n:
            bit_count = 0
            tmp_num = i
            while tmp_num != 0:
                lg_num = int(math.log2(tmp_num))
                bit_count += 1
                tmp_num = tmp_num - pow(2, lg_num)
            result.append(bit_count)
            i += 1
        return result


class Solution4:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        for i in range(1, n + 1):
            result[i] = result[i >> 1] + i % 2
        return result


a = Solution4()
print(a.countBits(1))
