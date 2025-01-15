# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursion
class Solution(object):
    def reverseOddLevels(self, root):
        self.queue = [root]
        self.tmp_queue = []
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        def bfs(queue, level):
            self.tmp_queue = []
            for node in queue:
                if node.left:
                    self.tmp_queue.append(node.left)
                if node.right:
                    self.tmp_queue.append(node.right)
            if not self.tmp_queue:
                return
            if level % 2 == 1:
                front = 0
                back = len(self.tmp_queue) - 1
                for i in range(len(self.tmp_queue) // 2):
                    self.tmp_queue[front].val, self.tmp_queue[back].val = self.tmp_queue[back].val, self.tmp_queue[
                        front].val
                    front += 1
                    back -= 1
            bfs(self.tmp_queue, level + 1)

        bfs(self.queue, 1)
        return root


# iterative approach
class Solution2(object):
    def reverseOddLevels(self, root):
        queue = [root]
        level = 1
        while True:
            if not queue:
                return root
            for i in range(len(queue)):
                if queue[i].left:
                    queue.append(queue[i].left)
                if queue[i].right:
                    queue.append(queue[i].right)
            queue = queue[2 ** (level - 1):]
            if level % 2 == 1:
                front = 0
                back = len(queue) - 1
                while front < back:
                    queue[front].val, queue[back].val = queue[back].val, queue[front].val
                    front += 1
                    back -= 1
            level += 1


# ChatGPT optimized Solution2
class Solution3(object):
    def reverseOddLevels(self, root):
        if not root:
            return root

        queue = [root]
        level = 0  # Начинаем с нулевого уровня

        while queue:
            # Формируем текущий уровень и следующее поколение
            next_level = []
            for node in queue:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            # Если уровень нечетный, разворачиваем значения
            if level % 2 == 1:
                left, right = 0, len(queue) - 1
                while left < right:
                    queue[left].val, queue[right].val = queue[right].val, queue[left].val
                    left += 1
                    right -= 1

            # Переходим на следующий уровень
            queue = next_level
            level += 1

        return root


# dfs approach
class Solution4(object):
    def reverseOddLevels(self, root):
        ...


tree = TreeNode(val=2, left=TreeNode(val=3, left=TreeNode(val=8), right=TreeNode(val=13)),
                right=TreeNode(val=5, left=TreeNode(val=21), right=TreeNode(val=34)))
# tree = TreeNode(val=0, left=TreeNode(val=1, left=TreeNode(val=0, left=TreeNode(val=1), right=TreeNode(val=1)),
#                                      right=TreeNode(val=0, left=TreeNode(val=1), right=TreeNode(val=1))),
#                 right=TreeNode(val=2, left=TreeNode(val=0, left=TreeNode(val=2), right=TreeNode(val=2)),
#                                right=TreeNode(val=0, left=TreeNode(val=2), right=TreeNode(val=2))))
a = Solution2()
print(a.reverseOddLevels(tree))
