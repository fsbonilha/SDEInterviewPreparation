# Problem: Longest Repeating Substring with Replacement

# Source:
# https://neetcode.io/problems/longest-repeating-substring-with-replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        right = 0
        left = 0
        charCount = {}
        longest = 0

        for right in range(len(s)):
            currChar = s[right]
            if currChar in charCount:
                charCount[currChar] += 1
            else:
                charCount[currChar] = 1
            mostFreq = max(charCount.values())

            while ((right - left + 1) - mostFreq) > k:
                charCount[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest
