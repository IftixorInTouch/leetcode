from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.inverted_tree = None

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.inverted_tree = TreeNode(val=root.val)

        def dfs(root, inverted_tree):
            if root.left:
                inverted_tree.right = TreeNode(val=root.left.val)
                dfs(root.left, inverted_tree.right)
            if root.right:
                inverted_tree.left = TreeNode(val=root.right.val)
                dfs(root.right, inverted_tree.left)

        dfs(root, self.inverted_tree)
        return self.inverted_tree


btree = TreeNode(val=4, left=TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3)),
                 right=TreeNode(val=7, left=TreeNode(val=6), right=TreeNode(val=9)))
a = Solution()
print(a.invertTree(btree))
