# Problem: Invert a Binary Tree

# Source: https://neetcode.io/problems/invert-a-binary-tree

# This recursive solution uses a base case where there are no children
# Then, it only exchanges the values of left and right for each Node up
# the tree.

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)

        return root
