from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head is not None and head.val == val:
            head = head.next
        current = head
        previous = None
        while current is not None:
            if current.val == val:
                if previous is not None:
                    previous.next = current.next
                current = current.next
            else:
                previous = current
                current = current.next
        return head


class Solution2:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)

        current = dummy
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next


a = Solution2()
b = ListNode(1)
b.next = ListNode(6)
b.next.next = ListNode(2)
b.next.next.next = ListNode(0)
# b.next.next.next.next = ListNode(4)
# b.next.next.next.next.next = ListNode(5)
# b.next.next.next.next.next.next = ListNode(6)

test = (a.removeElements(b, 6))
while test is not None:
    print(test.val)
    test = test.next
