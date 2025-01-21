class QuicKSort:

    def sort(self, nums):
        if len(nums) < 2:
            return nums
        middle = len(nums) // 2
        pivot = nums[middle]  # can be any pivot
        left = [num for num in nums if num < pivot]
        right = [num for num in nums if num > pivot]
        equal = [num for num in nums if num == pivot]
        return self.sort(left) + equal + self.sort(right)


a = QuicKSort()
print(a.sort([2, 6, 1, 4, 3, 7, 6, 8, 5]))
