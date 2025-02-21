from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        distances = []
        for num in arr:
            distances.append(abs(num - x))

        min_distance = float('inf')
        min_distance_id = -1

        for idx, num in enumerate(distances):
            if num < min_distance:
                min_distance = num
                min_distance_id = idx

        left = min_distance_id
        right = min_distance_id

        result = []

        while abs(right - left) != k:
            if left == right:
                result.append(arr[left])
                left -= 1
                right += 1
                continue
            if left < 0 and right >= len(distances):
                return result
            if left < 0:
                result.append(arr[right])
                right += 1
                continue
            if right >= len(distances):
                result.append(arr[left])
                left -= 1
                continue
            if distances[left] <= distances[right]:
                result.append(arr[left])
                left -= 1
            elif distances[right] < distances[left]:
                result.append(arr[right])
                right += 1

        return result


a = Solution()
print(a.findClosestElements([1, 2, 3, 4, 5], 4, 3))
