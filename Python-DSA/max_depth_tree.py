
 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def get_depth(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left_len = get_depth(node.left)
            right_len = get_depth(node.right)
            return max(left_len, right_len) + 1

        return get_depth(root)
