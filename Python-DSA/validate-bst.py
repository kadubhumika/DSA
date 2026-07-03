from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check_bst(root_node, left_range, right_range):

            if root_node == None:
                return True

            if root_node.val <= left_range or root_node.val >= right_range:
                return False

            left_subtree = check_bst(
                root_node.left,
                left_range,
                root_node.val
            )

            right_subtree = check_bst(
                root_node.right,
                root_node.val,
                right_range
            )

            return left_subtree and right_subtree

        return check_bst(root, float('-inf'), float('inf'))