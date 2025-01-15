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


a = Solution()
b = ListNode(1)
b.next = ListNode(2)
b.next.next = ListNode(3)
b.next.next.next = ListNode(2)
b.next.next.next.next = ListNode(1)
print(a.isPalindrome(b))
