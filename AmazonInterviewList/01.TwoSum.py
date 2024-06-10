# Source: https://leetcode.com/problems/two-sum/?envType=problem-list-v2&envId=954v5ops

# Problem: Two Sum

# Example: Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# BASELINE SOLUTION - O(N^2)
# def twoSum(self, nums: List[int], target: int) -> List[int]:
#     length = len(nums)
#     for i in range(length - 1):
#         for j in range(i + 1, length):
#             if (nums[i] + nums[j]) == target:
#                 return [i, j]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_indexed = [(num, i) for i, num in enumerate(nums)]
        nums_indexed.sort()

        start = 0
        end = len(nums) - 1
        while(end > start):
            current_sum = nums_indexed[start][0] + nums_indexed[end][0]
            if current_sum == target:
                return [nums_indexed[start][1], nums_indexed[end][1]]
            elif current_sum > target:
                end -= 1
            else:
                start += 1
        return [] # Error
            

