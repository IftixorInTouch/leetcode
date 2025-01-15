from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        lst = []
        while head is not None:
            lst.append(head)
            head = head.next
        lst = list(reversed(lst))
        previous_node = lst[0]
        for node in lst[1:]:
            previous_node.next = node
            previous_node = node
        lst[-1].next = None
        return lst[0]


class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return head
        previous = current = head
        current = current.next
        head = head.next.next
        previous.next = None
        while current is not None:
            current.next = previous
            previous = current
            current = head
            if head is not None:
                head = head.next
        return previous


a = Solution2()
b = ListNode(1)
b.next = ListNode(2)
b.next.next = ListNode(3)
b.next.next.next = ListNode(4)
b.next.next.next.next = ListNode(5)
rev_list = a.reverseList(b)
while rev_list is not None:
    print(rev_list.val)
    rev_list = rev_list.next
