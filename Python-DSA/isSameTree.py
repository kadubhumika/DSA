class Solution(object):
    def isSameTree(self, p, q):
        # If both nodes are None, they are identical
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
