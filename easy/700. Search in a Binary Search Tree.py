# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node, val):
            if val > node.val:
                if node.right:
                    return dfs(node.right, val)
                else:
                    return None
            elif val < node.val:
                if node.left:
                    return dfs(node.left, val)
                else:
                    return None
            else:
                return node

        return dfs(root, val)


tree = TreeNode(val=4, left=TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3)), right=TreeNode(val=7))
# tree = TreeNode(val=5)
a = Solution()
print(a.searchBST(tree, 5))
