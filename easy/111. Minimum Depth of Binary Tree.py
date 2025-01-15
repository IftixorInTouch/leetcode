from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            if not root.left and root.right:
                return 1 + dfs(root.right)
            elif not root.right and root.left:
                return 1 + dfs(root.left)
            else:
                return 1 + min(dfs(root.left), dfs(root.right))
        return dfs(root)


class Solution2:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = [root]
        depth = 1
        while queue:
            n = len(queue)
            for i in range(n - 1, -1, -1):
                node = queue.pop(i)
                if node.left is None and node.right is None:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1


btree = TreeNode(val=1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3))
a = Solution2()
print(a.minDepth(btree))
