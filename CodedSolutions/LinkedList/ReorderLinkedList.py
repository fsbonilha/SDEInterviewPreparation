# Problem: Reorder Linked List

# Source: https://neetcode.io/problems/reorder-linked-list


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Split the list in half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        first = head

        second = slow.next
        slow.next = None

        prev = None
        # Reorder second list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        second = prev

        result = first
        # Merge Both Lists
        while first and second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

        return result
