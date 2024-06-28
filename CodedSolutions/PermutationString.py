# Problem: Permutation String

# Source: https://neetcode.io/problems/permutation-string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        left = 0
        right = length - 1
        countsS1 = {}

        for letter in s1: 
            countsS1[letter] = 1 + countsS1.get(letter, 0)

        while right < len(s2):
            countsS2 = {}
            for letter in s2[left:right+1]:
                countsS2[letter] = 1 + countsS2.get(letter, 0)
            if countsS2 == countsS1:
                return True
            left += 1
            right += 1
        return False
