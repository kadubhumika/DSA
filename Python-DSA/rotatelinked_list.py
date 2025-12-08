# Definition for singly-linked list.
 class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return head

        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        n = len(arr)
        k = k % n

        if k == 0:
            return head

        arr.reverse()

        part1 = arr[:k]
        part2 = arr[k:]

        part1.reverse()
        part2.reverse()

        new_arr = part1 + part2

        dummy = ListNode(0)
        curr = dummy
        for val in new_arr:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next
