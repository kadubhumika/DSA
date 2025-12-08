
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):

        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        first = []  # numbers < x
        second = []  # numbers >= x

        for num in arr:
            if num < x:
                first.append(num)
            else:
                second.append(num)

        final = first + second

        dummy = ListNode(0)
        curr = dummy
        for val in final:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next
