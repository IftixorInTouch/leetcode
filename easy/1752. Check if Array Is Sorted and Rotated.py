from typing import List


#  Very large code
class Solution:
    """Very large code"""

    def check(self, nums: List[int]) -> bool:
        def rotate(first, second):
            left, right = 0, len(first) - 1
            while left < right:
                first[left], first[right] = first[right], first[left]
                left += 1
                right -= 1

            left, right = 0, len(second) - 1
            while left < right:
                second[left], second[right] = second[right], second[left]
                left += 1
                right -= 1

            return first + second

        def divide_arr_into_sorted_subarr(nums):
            divided_arr = [[nums[0]]]
            idx = 0
            for num in nums[1:]:
                if num < divided_arr[idx][-1]:
                    idx += 1
                    divided_arr.append([])
                divided_arr[idx].append(num)
            return divided_arr

        def is_sorted(nums):
            previous = nums[0]
            for num in nums[1:]:
                if num > previous:
                    return False
                previous = num
            return True

        nums = divide_arr_into_sorted_subarr(nums)

        if len(nums) == 1:
            return True
        elif len(nums) > 2:
            return False

        nums = rotate(nums[0], nums[1])
        return is_sorted(nums)


class Solution2:
    def check(self, nums: List[int]) -> bool:
        idx = 1
        previous = nums[0]
        for num in nums[1:]:
            if num < previous:
                break
            idx += 1
            previous = num

        if idx == len(nums):
            return True

        previous = nums[idx]
        idx = (idx + 1) % len(nums)
        for i in range(len(nums) - 1):
            if nums[idx] < previous:
                return False
            previous = nums[idx]
            idx = (idx + 1) % len(nums)
        return True


a = Solution2()
print(a.check([3, 4, 5, 1, 2]))
