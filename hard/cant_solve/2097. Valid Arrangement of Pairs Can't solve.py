from typing import List


# Cant solve it, there may cycles in the graph
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]
        result = []
        linked_list_dict = {}
        for pair in pairs:
            linked_list_dict.update({pair[0]: pair[1]})
        print(linked_list_dict)
        unique_vertexes = {}
        for pair in pairs:
            if pair[0] not in unique_vertexes:
                unique_vertexes.update({pair[0]: 0})
            if pair[1] not in unique_vertexes:
                unique_vertexes.update({pair[1]: 0})
        print(unique_vertexes)
        head = None
        for node_value in unique_vertexes:
            if node_value not in linked_list_dict.values():
                head = node_value
                break
        if head is None:
            head = pairs[0][0]
        for node in linked_list_dict:
            result.append([head, linked_list_dict[head]])
            head = linked_list_dict[head]
        return result


a = Solution()

test = [[1, 2], [1, 3], [2, 1]]
print(a.validArrangement(test))
