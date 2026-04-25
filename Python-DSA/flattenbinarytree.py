class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        result = []

        def preorder(node):
            if not node:
                return

            result.append(node)
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        # now convert list into linked list
        for i in range(len(result) - 1):
            result[i].left = None
            result[i].right = result[i + 1]