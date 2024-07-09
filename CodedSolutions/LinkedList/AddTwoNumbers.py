# Problem: Add Two Numbers

# Source: https://neetcode.io/problems/add-two-numbers


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        sumTail = dummy
        toNextDigit = 0
        n1 = l1
        n2 = l2

        while n1 or n2 or toNextDigit:
            currSum = toNextDigit
            if n1:
                currSum += n1.val
            if n2:
                currSum += n2.val

            if currSum >= 10:
                currSum -= 10
                toNextDigit = 1
            else:
                toNextDigit = 0

            sumTail.next = ListNode(currSum)
            sumTail = sumTail.next

            if n1:
                n1 = n1.next
            if n2:
                n2 = n2.next

        return dummy.next
