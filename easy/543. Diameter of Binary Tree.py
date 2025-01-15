from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def max_depth(root):
            if not root:
                return 0
            left = max_depth(root.left)
            right = max_depth(root.right)

            self.diameter = max(self.diameter, left + right)

            return max(left, right) + 1

        max_depth(root)
        return self.diameter


btree = TreeNode(val=1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3))
a = Solution()
print(a.diameterOfBinaryTree(btree))
