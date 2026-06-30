# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        # val stores the value, next points to the next node
         self.val = val
         self.next = next
from typing import Optional


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        n = 0
        current = head
        while current:
            n += 1
            current = current.next

        mid = n // 2

        current = head
        for _ in range(mid):
            current = current.next

        return current
