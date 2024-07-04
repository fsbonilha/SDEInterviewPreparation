# Problem: Find Minimum in Rotated Sorted Array

# Source: https://neetcode.io/problems/find-minimum-in-rotated-sorted-array

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1
        result = nums[0]

        while left <= right:
            mid = left + (right - left) // 2
            result = min(result, nums[mid])

            # Sorted
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break
            elif nums[mid] >= nums[left]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid - 1
        return result
