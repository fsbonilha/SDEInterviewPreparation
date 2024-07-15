# Problem: Depth of a Binary Tree

# Source: https://neetcode.io/problems/depth-of-binary-tree

# Solution: This algorithm uses a recursive approach, that calls
# itself in each of the left/right children and adds 1 to the
# current max result (left and right trees).
#
# It also returns zero if called with a None node, to avoid
# unnecessary ifs and no need to return 1 when end is reached.

# Complexity: O(N)

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        return max(leftDepth, rightDepth) + 1
