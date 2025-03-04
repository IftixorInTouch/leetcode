class SelectionSort:

    def sort(self, array):

        for i in range(len(array)):
            minimum = [float('inf'), -1]
            for j in range(i, len(array)):
                if array[j] < minimum[0]:
                    minimum = [array[j], j]
            tmp = array[i]
            array[i] = minimum[0]
            array[minimum[1]] = tmp
        return array


a = SelectionSort()
print(a.sort([2, 6, 1, 4, -1, 0, -1, 3, 7, 6, 8, 5]))
