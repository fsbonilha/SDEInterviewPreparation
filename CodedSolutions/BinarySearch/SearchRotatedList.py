# Problem: Find Target in Rotated Sorted Array

# Source: https://neetcode.io/problems/find-target-in-rotated-sorted-array

# Divide the array into two partitions, and find out in what partition the
# number is. Then, it sort of works like a normal Binary Search.

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.search_rec(nums, target, 0, len(nums) - 1)

    def search_rec(self, nums: List[int], target: int, left: int, right: int):
        if left > right:
            return -1

        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid

        # target is in right partition
        if target <= nums[right]:
            # mid is in left partition ?
            if nums[mid] > nums[right] or target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
        # target is in left partition
        else:
            # mid is in right partition?
            if nums[mid] < nums[right] or target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1

        return self.search_rec(nums, target, left, right)
