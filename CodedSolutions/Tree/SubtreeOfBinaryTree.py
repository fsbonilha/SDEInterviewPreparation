# Problem: Subtree of a Binary Tree

# Source: https://neetcode.io/problems/subtree-of-a-binary-tree

# Solution: This solution uses a recursive approach, and at each
# node, the solution checks if the tree that is left is the same
# of the subtree

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode],
                  subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return (self.isSubtree(root.right, subRoot) or
                self.isSubtree(root.left, subRoot))

    def isSameTree(self, root1: Optional[TreeNode],
                   root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if root1 and root2 and root1.val == root2.val:
            return (self.isSameTree(root1.left, root2.left) and
                    self.isSameTree(root1.right, root2.right))
        return False
