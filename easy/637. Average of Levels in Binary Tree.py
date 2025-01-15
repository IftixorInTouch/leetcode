from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [root]
        result = []
        while queue:

            n = len(queue)
            level_sum = 0
            for i in range(n - 1, -1, -1):
                node = queue.pop(i)
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_sum / n)
        return result
