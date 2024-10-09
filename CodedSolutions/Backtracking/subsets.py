# Problem: Subsets

# Source: https://neetcode.io/problems/subsets

# Solution: Depth-First Search (DFS) over the tree of possibilities
# (include vs not include a number in the subset), then backtrack and
# repeat the process until all numbers are convered (base case)

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                results.append(subset.copy())
                return
            # add next number and continue
            subset.append(nums[i])
            dfs(i + 1)

            # remove the number just added and continue
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return results
