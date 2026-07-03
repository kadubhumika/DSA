from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        def dfs(node, current_sum):

            current_sum += node.val

            if not node.left and not node.right:
                return current_sum == targetSum

            if node.left:
                if dfs(node.left, current_sum):
                    return True

            if node.right:
                if dfs(node.right, current_sum):
                    return True

            return False

        return dfs(root, 0)
