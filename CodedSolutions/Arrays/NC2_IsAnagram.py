# Source: https://neetcode.io/problems/is-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterSetS = self.countLetters(s)
        letterSetT = self.countLetters(t)
        if letterSetS == letterSetT:
            return True
        else:
            return False

    def countLetters(self, s: str) -> dict:
        letterSet = dict()
        for letter in s:
            if letter in letterSet.keys():
                letterSet[letter] += 1
            else:
                letterSet[letter] = 1
        return letterSet
