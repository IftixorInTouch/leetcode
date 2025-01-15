from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and root2:
            return root2

        def dfs(root1, root2):
            if not root2:
                return
            root1.val += root2.val
            if not root1.left and root2.left:
                root1.left = TreeNode(val=root2.left.val)
                root2.left.val = 0
            if not root1.right and root2.right:
                root1.right = TreeNode(val=root2.right.val)
                root2.right.val = 0

            dfs(root1.left, root2.left)
            dfs(root1.right, root2.right)

        dfs(root1, root2)
        return root1


btree1 = TreeNode(val=1, left=TreeNode(val=3, left=TreeNode(val=5)), right=TreeNode(val=2))
btree2 = TreeNode(val=2, left=TreeNode(val=1, right=TreeNode(val=4)), right=TreeNode(val=3, right=TreeNode(val=7)))
a = Solution()
print(a.mergeTrees(btree1, btree2))


class Solution2:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1

        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1
