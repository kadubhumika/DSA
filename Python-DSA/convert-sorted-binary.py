# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return None

        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next

        def build_bst(left_index: int, right_index: int) -> Optional[TreeNode]:
            if left_index > right_index:
                return None
            mid = left_index + (right_index - left_index) // 2
            node = TreeNode(arr[mid])
            node.left = build_bst(left_index, mid - 1)
            node.right = build_bst(mid + 1, right_index)
            return node

        return build_bst(0, len(arr) - 1)
