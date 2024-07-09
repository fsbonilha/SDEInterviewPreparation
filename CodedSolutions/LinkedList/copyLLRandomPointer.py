# Problem: Copy Linked List with Random Pointer

# Source: https://neetcode.io/problems/copy-linked-list-with-random-pointer

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {}
        dummy = Node(0)
        tail = dummy

        current = head
        while current:
            new = Node(current.val)
            tail.next = new
            oldToCopy[current] = new

            tail = tail.next
            current = current.next

        current = head
        new = dummy.next
        while current:
            if current.random:
                new.random = oldToCopy[current.random]

            new = new.next
            current = current.next

        return dummy.next
