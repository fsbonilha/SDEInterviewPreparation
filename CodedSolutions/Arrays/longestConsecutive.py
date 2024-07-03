# Source: https://neetcode.io/problems/longest-consecutive-sequence

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0
        for num in numsSet:
            if num - 1 in numsSet:
                continue

            currentNum = num
            size = 1
            while currentNum + 1 in numsSet:
                size += 1
                currentNum += 1
            if size > longest:
                longest = size
        return longest
