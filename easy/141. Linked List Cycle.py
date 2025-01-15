from typing import Optional


# head = [3,2,0,-4]

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class List:
    def __init__(self, head: ListNode):
        self.head = head


class Solution1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        second_head = head
        i = 1
        while head.next is not None:
            if i % 2 == 0:
                second_head = second_head.next
            head = head.next
            if head == second_head:
                return True
            i += 1
        return False


class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        lst = []
        while head.next is not None:
            if head in lst:
                return True
            lst.append(head)
            head = head.next
        return False


a = Solution1()
c = ListNode(2)
b = List(ListNode(3))
b.head.next = c
b.head.next.next = ListNode(0)
b.head.next.next.next = ListNode(-4)
b.head.next.next.next.next = c
print(a.hasCycle(b.head))
