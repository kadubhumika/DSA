from typing import Optional, List  # Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 1. Handle empty input edge cases safely
        if not lists:
            return None

        # 2. Extract values from the linked lists into a flat Python list
        flat_list = []
        for head in lists:
            current = head
            while current:
                flat_list.append(current.val)
                current = current.next

        # 3. Sort the extracted flat list of numbers
        flat_list.sort()

        # 4. Rebuild a brand-new sorted linked list from the sorted values
        dummy = ListNode(0)
        current = dummy
        for value in flat_list:
            current.next = ListNode(value)
            current = current.next

        return dummy.next