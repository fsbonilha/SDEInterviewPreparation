# Problem: Binary Tree Diameter

# Source: https://neetcode.io/problems/binary-tree-diameter

# Solution: This recursive solution computes for each node
# what is the sum of the max heights in each of the nodes.
# It also keeps track of a result variable with the max
# found value, and updates it if needed.

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depthFirstSearch(root)
        return self.result

    def depthFirstSearch(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftHeight = self.depthFirstSearch(root.left)
        rightHeight = self.depthFirstSearch(root.right)
        # diameter of tree
        self.result = max(self.result, leftHeight + rightHeight)

        return 1 + max(leftHeight, rightHeight)
