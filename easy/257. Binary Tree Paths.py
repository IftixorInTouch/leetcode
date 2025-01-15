from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        path = ""
        def dfs(root, path):
            if not path:
                path += f"{root.val}"
            else:
                path += f"->{root.val}"
            if not root.left and not root.right:
                result.append(path)
                return path
            if root.left:
                dfs(root.left, path)
            if root.right:
                dfs(root.right, path)
        dfs(root, path)
        return result


btree = TreeNode(val=1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3))
a = Solution()
print(a.binaryTreePaths(btree))