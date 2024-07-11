# Problem: Find Duplicate Integer --> O(1) space - Required Floyd's Cycle

# Source: https://neetcode.io/problems/find-duplicate-integer

# This algorithm uses a fast and slow pointer, let's call the meeting point X,
# the Distance(X, startOfCycle) is equal to Distance(startOfCycle, origin)
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        # Walk fast and slow until they meet - the X point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break

        # Now, walk from origin until it meets with the previous slow
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                break
        return slow

# Basic solution O(n) space and O(n) speed using a HashSet

# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         found = set()
#         for num in nums:
#             if num in found:
#                 return num
#             else:
#                 found.add(num)
