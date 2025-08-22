class CountingSort:

    def sort(self, array):
        """Sorting small positive integers"""
        counter_dict = [0] * (max(array) + 1)
        output = [0] * len(array)

        for i in range(len(array)):
            counter_dict[array[i]] += 1

        for i in range(1, len(counter_dict)):
            counter_dict[i] += counter_dict[i - 1]

        for i in range(len(array) - 1, -1, -1):
            output[counter_dict[array[i]] - 1] = array[i]
            counter_dict[array[i]] -= 1

        return output


a = CountingSort()
print(a.sort([2, 6, 1, 4, 3, 7, 6, 8, 5]))
print(a.sort([2, 6, 1, 4, -1, 0, -1, 3, 7, 6, 8, 5]))
