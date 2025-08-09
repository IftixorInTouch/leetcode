from typing import List


class Solution:
    """
    Time Complexity: O(2^n)
    Memory limit exceeded
    """

    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        target = nums_sum // 2
        mask = self.make_bit_mask(len(nums))
        sums = []

        for bits_idx, bits in enumerate(mask):
            cur_sum = 0
            for bit_idx, bit in enumerate(bits):
                if bit == 1:
                    cur_sum += nums[bit_idx]
            if cur_sum == target:
                sums.append((bits_idx, cur_sum))

        for i in range(len(sums)):
            for j in range(i + 1, len(sums)):
                answer = 0
                for k in range(len(nums)):
                    if mask[sums[i][0]][k] == mask[sums[j][0]][k]:
                        break
                    answer += 1
                if answer == len(nums):
                    return True
        return False

    def make_bit_mask(self, n):
        mask = []
        for i in range(2 ** n):
            bit = [0] * n
            bit_idx = 0
            while i != 0:
                bit[bit_idx] = i % 2
                bit_idx += 1
                i = i // 2
            mask.append(bit)
        return mask


a = Solution()
print(a.canPartition(
    [15, 56, 4, 1, 7, 80, 88, 22, 35, 69, 23, 24, 73, 14, 14, 3, 2, 5, 60, 95, 68, 55, 81, 96, 71, 51, 93, 5, 53, 37,
     29, 64, 58, 1, 83, 67, 26, 53, 3, 44, 35, 2, 43, 37, 18, 30, 61, 55, 40, 81, 35, 3, 2, 23, 86, 3, 73, 93, 73, 30,
     22, 47, 20, 97, 57, 16, 40, 100, 100, 84, 97, 5, 45, 12, 33, 92, 95, 26, 94, 41, 60, 22, 65, 9, 35, 62, 85, 62, 3,
     4, 5, 64, 98, 61, 46, 4, 88, 71, 13, 45, 53, 46, 70, 69, 43, 55, 23, 51, 11, 1, 89, 86, 45, 81, 1, 94, 5, 99, 74,
     95, 8, 89, 28, 48, 27, 64, 27, 31, 12, 41, 45, 34, 57, 64, 95, 65, 72, 69, 77, 14, 7, 39, 6, 8, 67, 1, 82, 25, 18,
     73, 17, 10, 52, 70, 82, 47, 70, 86, 14, 91, 67, 34, 37, 10, 87, 26, 42, 41, 7, 81, 29, 49, 45, 80, 38, 58, 1, 54,
     53, 52, 23, 31, 85, 69, 52, 25, 37, 45, 66, 22, 56, 31, 23, 9, 2, 88, 9, 92, 44, 21]))
