from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        current = slow.next
        previous = None
        slow.next = None

        while current:
            tmp_next = current.next
            current.next = previous
            previous = current
            current = tmp_next

        first = head
        second = previous
        while second:
            tmp_1, tmp_2 = first.next, second.next
            first.next = second
            second.next = tmp_1
            first, second = tmp_1, tmp_2


lst = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4))))

a = Solution()
print(a.reorderList(lst))
