# Source: https://leetcode.com/problems/merge-k-sorted-lists/

# Problem: Merge K Sorted Lists

# Questions: 
# 1. Can we have empty cases?
# 2. How big can a value be in this problem? 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        tail = None
        emptyList = [None] * len(lists)
        while lists != emptyList:
            minVal = (10**4 + 1)
            minHead = None
            for index, currHead in enumerate(lists):
                if currHead is not None and currHead.val < minVal:
                    minVal = currHead.val
                    minHead = index
            lists[minHead] = lists[minHead].next
            newNode = ListNode(minVal)
            if head is None:
                head = newNode
                tail = newNode
            else:
                tail.next = newNode
                tail = newNode
        return head

                
                

