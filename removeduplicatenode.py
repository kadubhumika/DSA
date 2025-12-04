class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return head

        fix = head
        fix_val = fix.val
        curr = fix.next

        while curr:
            if curr.val == fix_val:
                curr = curr.next
            else:
                fix.next = curr
                fix = curr
                fix_val = curr.val
                curr = curr.next

        fix.next = None
        return head
