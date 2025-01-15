from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def dfs(root, head):
            if not head:
                return True
            if not root:
                return False
            if root.val != head.val:
                return False
            return dfs(root.left, head.next) or dfs(root.right, head.next)

        if not root:
            return False

        return dfs(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


#
# lst = ListNode(val=1, next=ListNode(val=2))
# tree = TreeNode(val=0, left=TreeNode(val=1, left=TreeNode(val=3), right=TreeNode(val=3)),
#                 right=TreeNode(val=2, left=TreeNode(val=1, left=TreeNode(val=3), right=TreeNode(val=2))))
lst = ListNode(val=4, next=ListNode(val=2))
tree = TreeNode(val=4, left=TreeNode(val=4, left=TreeNode(val=1, left=TreeNode(val=2))), right=TreeNode(val=4))
# lst = ListNode(val=1, next=ListNode(val=4, next=ListNode(val=2, next=ListNode(val=6))))
# tree = TreeNode(val=1, left=TreeNode(val=4, right=TreeNode(val=2, left=TreeNode(val=1))), right=TreeNode(val=4,
#                                                                                                          left=TreeNode(
#                                                                                                              val=2,
#                                                                                                              left=TreeNode(
#                                                                                                                  val=6),
#                                                                                                              right=TreeNode(
#                                                                                                                  val=8,
#                                                                                                                  left=TreeNode(
#                                                                                                                      val=1),
#                                                                                                                  right=TreeNode(
#                                                                                                                      val=3)))))

# lst = ListNode(val=3)
# tree = TreeNode(val=1, left=TreeNode(val=5, right=TreeNode(val=4)), right=TreeNode(val=3, right=TreeNode(val=3)))
a = Solution()

print(a.isSubPath(lst, tree))
