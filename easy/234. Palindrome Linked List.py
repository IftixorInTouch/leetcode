from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        counter = 0
        while head is not None:
            lst.append(head.val)
            head = head.next
            counter += 1
        for (left, right) in zip(lst[:int(counter / 2)], lst[:int(counter / 2) - 1: -1]):
            if left - right != 0:
                return False
        return True


class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        middle = self.middleNode(head)
        reverse = self.reverseList(middle)
        while reverse:
            if reverse.val != head.val:
                return False
            reverse = reverse.next
            head = head.next
        return True

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


a = Solution()
b = ListNode(1)
b.next = ListNode(2)
b.next.next = ListNode(3)
b.next.next.next = ListNode(2)
b.next.next.next.next = ListNode(1)
print(a.isPalindrome(b))
