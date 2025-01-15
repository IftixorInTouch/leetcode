from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.flag = True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and not q:
            return False
        if q and not p:
            return False
        def dfs(p, q):
            if p.val != q.val:
                self.flag = False
            if p.left and q.left:
                dfs(p.left, q.left)
            if p.right and q.right:
                dfs(p.right, q.right)
            if (p.left and not q.left) or (not p.left and q.left) or (p.right and not q.right) or (not p.right and q.right):
                self.flag = False

        dfs(p, q)
        return self.flag


class Solution2:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Are both p and q None?
        if not p and not q:
            return True

        # Is one of them None?
        if not p or not q:
            return False

        # Are their values different?
        if p.val != q.val:
            return False

        # Recursive call to the next level down
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
