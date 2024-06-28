# Problem: Longest Substring Without Duplicates

# Source: https://neetcode.io/problems/longest-substring-without-duplicates

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        longest = 0
        alreadySeen = dict()

        while right < len(s):
            currValue = s[right]
            if s[right] in alreadySeen:
                left = max(left, alreadySeen[currValue] + 1)
            alreadySeen[currValue] = right
            currLength = (right - left + 1)

            longest = max(longest, currLength)

            right += 1
        return longest
