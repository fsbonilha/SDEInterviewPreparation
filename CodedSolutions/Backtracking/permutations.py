# Problem: Permutations

# Source: https://neetcode.io/problems/permutations

# Solution: This solution uses a recursive function (DFS)
# in the decision tree that iterates over all numbers and
# appends one that is still not in the set, then it pops and
# go to the next num, until all possibilities are covered

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(current):
            if len(current) == len(nums):
                result.append(current.copy())
                return

            for num in nums:
                if num not in current:
                    current.append(num)
                    backtrack(current)
                    current.pop()
        backtrack([])
        return result
