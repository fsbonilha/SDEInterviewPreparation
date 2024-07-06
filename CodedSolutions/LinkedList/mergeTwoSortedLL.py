# Problem: Merge Two Sorted Linked Lists

# Source: https://neetcode.io/problems/merge-two-sorted-linked-lists

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        item1, item2 = list1, list2

        dummy = ListNode()
        tail = dummy

        while item1 and item2:
            if item1.val < item2.val:
                tail.next = item1
                item1 = item1.next
            else:
                tail.next = item2
                item2 = item2.next
            tail = tail.next

        if item1:
            tail.next = item1
        elif item2:
            tail.next = item2

        return dummy.next

# First Solution (Long):
#            
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode],
#                       list2: Optional[ListNode]) -> Optional[ListNode]:
#         item1, item2 = list1, list2

#         merged = None
#         mergedHead = None

#         while item1 and item2:
#             if item1.val <= item2.val:
#                 if merged:
#                     merged.next = item1
#                     merged = merged.next
#                 else:
#                     merged = item1
#                     mergedHead = merged
#                 item1 = item1.next
#             else:
#                 if merged:
#                     merged.next = item2
#                     merged = merged.next
#                 else:
#                     merged = item2
#                     mergedHead = merged
#                 item2 = item2.next

#         while item1:
#             if merged:
#                 merged.next = item1
#                 merged = merged.next
#             else:
#                 merged = item1
#                 mergedHead = merged
#             item1 = item1.next

#         while item2:
#             if merged:
#                 merged.next = item2
#                 merged = merged.next
#             else:
#                 merged = item2
#                 mergedHead = merged
#             item2 = item2.next

#         return mergedHead
