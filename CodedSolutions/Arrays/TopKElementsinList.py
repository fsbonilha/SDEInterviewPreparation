# Problem: Top K Elements in List

# Source: https://neetcode.io/problems/top-k-elements-in-list

# Complexity: O(n)

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countsMap = {}
        for num in nums:
            if num in countsMap.keys():
                countsMap[num] += 1
            else:
                countsMap[num] = 1

        counts = [[] for i in range(len(nums) + 1)]
        for index, count in countsMap.items():
            counts[count] += [index]

        solution = []
        for index in range(len(counts) - 1, 0, -1):
            for num in counts[index]:
                solution.append(num)
                if len(solution) == k:
                    return solution
