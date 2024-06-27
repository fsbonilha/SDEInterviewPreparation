# Problem: Max Water Container

# Source: https://neetcode.io/problems/max-water-container

# Questions: 
# 1. How can I calculate the amount of water?
# Answer: MIN(a,b) * dist(a,b), where a,b are elements in heights and
# dist is the distance between a,b elements

# Logic: When the opposite element is greater or equal, the
# capacity for that height can't get any bigger, so we can skip
# this specific height, so we keep skipping always the smaller
# height.

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        biggest = 0

        start = 0
        end = length - 1
        while start < end:
            capacity = min(heights[start], heights[end]) * (end - start)
            if capacity > biggest:
                biggest = capacity

            if heights[start] > heights[end]:
                end -= 1
            elif heights[start] < heights[end]:
                start += 1
            else:
                start += 1
                end -= 1
        return biggest
            
