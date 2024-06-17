# Source: https://leetcode.com/problems/longest-palindromic-substring/

# Problem: Longest Palindromic Substring 

# Brute Force Solution

class Solution:
    def longestPalindrome(self, s: str) -> str:
        index = 0
        start = 0
        longest = 0
        longest_start = 0
        longest_end = 0
        for start in range( , len(s)):
            for end in range(start, len(s)):
                word = s[start:end + 1]
                if self.isPalindrome(word) and len(word) > longest:
                    longest = len(word)
                    longest_start = start
                    longest_end = end + 1
        return s[longest_start:longest_end]

                
    def isPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        return False



# Center Expansion around every letter

# Complexity: O(nˆ2)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 1
        startLongest = 0
        endLongest = 1
        self.length = len(s)
        self.s = s
        for index in range(1, self.length):
            left, right = self.searchPalindrome(index, index) # Single Pivot
            if (right - left + 1) > longest:
                longest = (right - left + 1)
                startLongest = left
                endLongest = right + 1
            
            if s[index - 1] == s[index]:
                left, right = self.searchPalindrome(index - 1, index) # Double Pivot
                if (right - left + 1) > longest:
                    longest = (right - left + 1)
                    startLongest = left
                    endLongest = right + 1
            
        return s[startLongest:endLongest]

    def searchPalindrome(self, left, right) -> (int, int):
        while left - 1 >= 0 and right + 1 < self.length and (self.s[left - 1] == self.s[right + 1]):
            left -= 1
            right += 1
        return (left, right)