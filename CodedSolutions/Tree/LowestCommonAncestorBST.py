# Problem: Lowest Common Ancestor in Binary Search Tree

# Source:
# https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree

# Solution: The solution is based in recursevely visiting each node
# until a value is found or (using BST rule) a node are at separate
# parts.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode,
                             p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val == p or root.val == q:
            return root
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
