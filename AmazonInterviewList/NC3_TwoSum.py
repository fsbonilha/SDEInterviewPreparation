# Source: https://neetcode.io/problems/two-integer-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        alreadySeen = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in alreadySeen.keys():
                return [alreadySeen[diff], index]
            alreadySeen[num] = index
        return []
