# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len_a = 0
        temp = headA
        while temp:
            len_a += 1
            temp = temp.next
        len_b = 0
        temp = headB
        while temp:
            len_b += 1
            temp = temp.next

        diff = abs(len_a - len_b)

        currA = headA
        currB = headB
        if len_a > len_b:
            for _ in range(diff):
                currA = currA.next
        else:
            for _ in range(diff):
                currB = currB.next

        while currA != currB:
            currA = currA.next
            currB = currB.next
        return currA
