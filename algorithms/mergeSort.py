class MergeSort:

    def recursive_sort(self, array):
        if len(array) <= 1:
            return array
        left, right = array[:len(array) // 2], array[len(array) // 2:]
        self.recursive_sort(left)
        self.recursive_sort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

        return array

    def iterative_sort(self, array):
        pass


a = MergeSort()
print(a.recursive_sort([2, 6, 1, 4, -1, 0, -1, 3, 7, 6, 8, 5]))
print(a.recursive_sort([-1, 5, 0, 3, 7, 5]))
print(a.iterative_sort([2, 6, 1, 4, -1, 0, -1, 3, 7, 6, 8, 5]))
