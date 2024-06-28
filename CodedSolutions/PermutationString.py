# Problem: Permutation String

# Source: https://neetcode.io/problems/permutation-string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        left = 0
        right = length - 1
        countsS1 = {}

        self.addLetterToDict(s1, countsS1)

        while right < len(s2):
            countsS2 = {}
            self.addLetterToDict(s2[left:right+1], countsS2)
            if countsS2 == countsS1:
                return True
            left += 1
            right += 1
        return False

    def addLetterToDict(self, word: str, dictionary: dict):
        for letter in word:
            dictionary[letter] = 1 + dictionary.get(letter, 0)
