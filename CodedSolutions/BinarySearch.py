# Problem: Binary Search

# Source: https://neetcode.io/problems/binary-search

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.search_rec(nums, target, 0, len(nums)-1)

    def search_rec(self, nums: List[int], target: int,
                   left: int, right: int) -> int:
        mid = left + (right - left) // 2

        if left > right:
            return -1
        elif nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.search_rec(nums, target, left, mid - 1)
        else:
            return self.search_rec(nums, target, mid + 1, right)
