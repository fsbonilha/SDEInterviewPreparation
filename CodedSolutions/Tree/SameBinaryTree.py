# Problem: Same Binary Tree

# Source: https://neetcode.io/problems/same-binary-tree

# Solution: by using a recusive algorithm, the value of
# each node is compared, as well if the subtree below it
# also same. Finally, in the base case, both roots MUST
# be None, if not, the tree is different.

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False

        result = p.val == q.val

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return (result and left and right)
