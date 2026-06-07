# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
from typing import List, Optional


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:

        nodes = {}

        children = set()

        for p, c, d in descriptions:

            if p not in nodes:
                nodes[p] = TreeNode(p)

            if c not in nodes:
                nodes[c] = TreeNode(c)

            children.add(c)

            if d == 1:
                nodes[p].left = nodes[c]  # Instead of left.next
            elif d == 0:
                nodes[p].right = nodes[c]  # Instead of right.next

        for p, c, d in descriptions:
            if p not in children:
                return nodes[p]