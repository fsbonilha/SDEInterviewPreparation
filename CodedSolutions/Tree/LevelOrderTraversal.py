# Problem: Level Order Traversal of Binary Tree

# Source: https://neetcode.io/problems/level-order-traversal-of-binary-tree

# Solution: This solution is based on a Queue, where in each level, all
# children are added to the Queue after the current level has been
# processed. Every time the Queue is empty, the children of that Node are
# added.
from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque()
        if root:
            queue.append(root)

        while queue:
            qLen = len(queue)
            level = []
            for _ in range(qLen):
                current = queue.popleft()
                level.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            result.append(level)
        return result
