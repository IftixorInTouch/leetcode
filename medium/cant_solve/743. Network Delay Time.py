from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for node in times:
            elem = graph.get(node[0])
            if elem:
                elem.append([node[1], node[2]])
            else:
                graph[node[0]] = [[node[1], node[2]]]
        result = []
        visited = [k]
        visiting = k
        # while graph.get(visiting):
        #     node = graph[visiting].pop()
        #     if node[0] not in visited:
        #         visited.append(node[0])
        #         result += node[1]
        #     visiting = node[0]
        if len(visited) != n:
            return -1
        return min(result)


a = Solution()
print(a.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
