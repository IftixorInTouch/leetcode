# Definition for singly-linked list.
import random
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        if self.head is None:
            return None
        rand_int = random.randint(1, 10000)
        ls_length = 1
        tmp = self.head

        while rand_int != 0:
            if tmp.next is None:
                tmp = self.head
                rand_int %= ls_length
            else:
                tmp = tmp.next
            rand_int -= 1
            ls_length += 1

        return tmp.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
