from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
            self.val = val
            self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        while head is not None:
            lst.append(head)
            head = head.next
        half = int(len(lst) / 2)
        return lst[half]


a = Solution()
b = ListNode(1)
b.next = ListNode(2)
b.next.next = ListNode(3)
b.next.next.next = ListNode(4)
b.next.next.next.next = ListNode(5)
b.next.next.next.next.next = ListNode(6)
print(a.middleNode(b).val)
