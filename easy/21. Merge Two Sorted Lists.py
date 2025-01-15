from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        while list1 is not None:
            lst.append(list1.val)
            list1 = list1.next
        while list2 is not None:
            lst.append(list2.val)
            list2 = list2.next
        lst.sort()
        if not lst:
            return None
        new_list = ListNode(lst[0])
        list1 = new_list
        for val in lst[1:]:
            new_list.next = ListNode(val)
            new_list = new_list.next
        return list1


class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next


a = Solution2()
b = ListNode(1)
b.next = ListNode(2)
b.next.next = ListNode(4)

c = ListNode(1)
c.next = ListNode(1)
c.next.next = ListNode(2)
c.next.next.next = ListNode(4)
c.next.next.next.next = ListNode(4)
c.next.next.next.next.next = ListNode(5)
c.next.next.next.next.next.next = ListNode(6)

test = (a.mergeTwoLists(b, c))

while test is not None:
    print(test.val)
    test = test.next
