# Problem: Trapping Rain Water

# Source: https://neetcode.io/problems/trapping-rain-water

# Questions:
# 1. What's the output? The biggest "pool" of water? 
# Answer: No, it's the maximum water the WHOLE structure
# can trap. 

# What was difficult here? 

# Hard to get that the min of the tallest columns in 
# the right and left are what defines if the water is 
# collected or not. 

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        leftMax = [0 for _ in range(length)]
        rightMax = [0 for _ in range(length)]
        totalWater = 0

        currMax = 0
        for index in range(length - 1, -1, -1):
            rightMax[index] = currMax
            if height[index] > currMax:
                currMax = height[index]

        currMax = 0
        for index in range(length):
            leftMax[index] = currMax
            water = min(
                leftMax[index], 
                rightMax[index]
            ) - height[index]
            if water > 0:
                totalWater += water

            if height[index] > currMax:
                currMax = height[index]

        return totalWater
