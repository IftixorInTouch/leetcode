from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.has_path_sum = False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if (targetSum == root.val) and (not root.left) and (not root.right):
            self.has_path_sum = True
            return True
        if root.left:
            self.hasPathSum(root.left, targetSum - root.val)
        if root.right:
            self.hasPathSum(root.right, targetSum - root.val)
        return self.has_path_sum


btree = TreeNode(val=1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3))
a = Solution()
print(a.hasPathSum(btree, 9))
