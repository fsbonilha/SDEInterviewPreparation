# Problem: Balanced Binary Tree

# Source: https://neetcode.io/problems/balanced-binary-tree

# Solution: using a recursive approach, every node in the
# tree is checked to see if the difference in depth of
# right and left nodes are >1, it so, the tree is not
# balanced and the flag is set to False.
# The height of the subtree is returned in every step,
# while the flag is outside the recursion calls, in the
# object.


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalancedRecursive(root)
        return self.result

    def isBalancedRecursive(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 1

        leftDepth = self.isBalancedRecursive(root.left)
        rightDepth = self.isBalancedRecursive(root.right)

        if abs(leftDepth - rightDepth) > 1:
            self.result = False

        return 1 + max(leftDepth, rightDepth)
