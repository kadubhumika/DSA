from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        while curr:
            next_node = curr.next  # Save next node
            curr.next = prev  # Reverse the pointer
            prev = curr  # Move prev forward
            curr = next_node  # Move curr forward

        max_twin_sum = 0
        first_half = head
        second_half = prev

        while second_half:
            twin_sum = first_half.val + second_half.val
            if twin_sum > max_twin_sum:
                max_twin_sum = twin_sum

            first_half = first_half.next
            second_half = second_half.next

        return max_twin_sum
