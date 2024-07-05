# Problem: Reverse a Linked List

# Source: https://neetcode.io/problems/reverse-a-linked-list

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        currNode = head

        while currNode:
            nxt = currNode.next
            currNode.next = prev

            prev = currNode
            currNode = nxt
        return prev
