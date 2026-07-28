# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output = []

        def sum_node(node, sum_path, current_path):
            if not node:
                return

            sum_path += node.val
            current_path.append(node.val)

            if not node.left and not node.right:
                if sum_path == targetSum:
                    output.append(list(current_path))
            else:

                if node.left:
                    sum_node(node.left, sum_path, current_path)
                if node.right:
                    sum_node(node.right, sum_path, current_path)

            current_path.pop()

        if root:
            sum_node(root, 0, [])

        return output
