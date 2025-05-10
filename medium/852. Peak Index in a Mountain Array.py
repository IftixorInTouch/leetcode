from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 1
        right = len(arr) - 2

        while left <= right:
            middle = (left + right) // 2
            if arr[middle - 1] < arr[middle] > arr[middle + 1]:
                return middle
            elif arr[middle - 1] < arr[middle] < arr[middle + 1]:
                left = middle + 1
            else:
                right = middle - 1
