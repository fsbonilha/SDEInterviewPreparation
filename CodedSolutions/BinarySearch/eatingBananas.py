# Problem: Eating Bananas

# Source: https://neetcode.io/problems/eating-bananas

# Questions:
# 1. Can k be less the len(piles)? Answer: No, it is
# restricted

# Complexity: n log(n)

from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        top = max(piles)
        bottom = 1
        result = top

        while bottom <= top:
            mid = bottom + (top - bottom) // 2
            hoursConsumed = 0

            for pile in piles:
                hoursConsumed += math.ceil(pile / mid)

            if hoursConsumed > h:
                bottom = mid + 1
            elif hoursConsumed <= h:
                result = mid
                top = mid - 1
        return result
