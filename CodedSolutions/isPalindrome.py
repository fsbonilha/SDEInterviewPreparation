# Source: https://neetcode.io/problems/is-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = set("abcdefghijklmnopqrstuvwxyz01234567890")
        lower = s.lower()
        clean = ""

        for currChar in lower:
            if currChar in alpha:
                clean += currChar
        if clean == clean[::-1]:
            return True
        return False
