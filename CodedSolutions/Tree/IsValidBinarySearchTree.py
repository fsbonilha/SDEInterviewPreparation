# Problem: Is Valid Binary Search Tree

# Source: https://neetcode.io/problems/valid-binary-search-tree

# Solution: The solution is based on a Depth First Search (DFS),
# via a recursive approach. Besides from checking if node is between
# left and right, it's also necessary to check the min and max values
# of every subtree.


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    MIN_VAL = -1001
    MAX_VAL = 1001

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTRec(root)[0]

    def isValidBSTRec(self, root: Optional[TreeNode]):
        if not root:
            return (True, self.MAX_VAL, self.MIN_VAL)

        left = self.isValidBSTRec(root.left)
        right = self.isValidBSTRec(root.right)

        validNode = (left[2] < root.val and
                     right[1] > root.val)

        newMin = min(left[1], right[1], root.val)
        newMax = max(left[2], right[2], root.val)

        return (validNode and left[0] and right[0], newMin, newMax)
