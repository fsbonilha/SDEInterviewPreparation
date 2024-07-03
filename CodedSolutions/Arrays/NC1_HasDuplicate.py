# Source: https://neetcode.io/problems/duplicate-integer

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        already_seen = set()
        for num in nums:
            if num in already_seen:
                return True
            else:
                already_seen.add(num)
        return False
         