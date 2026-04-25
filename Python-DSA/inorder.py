class Solution:
    def inorderTraversal(self, root):
        result = []

        def helper(node):
            if node is None:
                return

            helper(node.left)

            result.append(node.val)

            helper(node.right)

        helper(root)
        return result