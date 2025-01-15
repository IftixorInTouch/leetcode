from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp_head = head
        while head and head.next is not None:
            if head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next
        return tmp_head


class Solution2:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        prev = head
        current = head.next
        while current:
            if current.val == prev.val:
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next
        return head


a = Solution1()
b = ListNode(1)
b.next = ListNode(1)
b.next.next = ListNode(1)
b.next.next.next = ListNode(1)
# b.next.next.next.next = ListNode(4)
# b.next.next.next.next.next = ListNode(5)
# b.next.next.next.next.next.next = ListNode(6)

test = (a.deleteDuplicates(b))
while test is not None:
    print(test.val)
    test = test.next
