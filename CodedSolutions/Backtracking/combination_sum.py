# Problem: Combination SUM to target

# Source: https://neetcode.io/problems/combination-target-sum

# Solution: Depth-First Search in the decision tree of appending
# the same number again or skipping to the next one, until it reaches
# the base case of finding the target, exceding the target or getting to
# the end of candidates pool


from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(idx, summed, total):
            if total == target:
                result.append(summed.copy())
                return
            if idx >= len(nums) or total > target:
                return

            summed.append(nums[idx])
            total += nums[idx]

            dfs(idx, summed, total)

            summed.pop()
            total -= nums[idx]

            dfs(idx + 1, summed, total)
        dfs(0, [], 0)
        return result
