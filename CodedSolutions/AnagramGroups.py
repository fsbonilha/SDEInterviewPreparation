# Source: https://neetcode.io/problems/anagram-groups

# Developed Solution: NeetCode

# Complexity: O(n * m)
# n = # of words
# m = average size of word

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letterCounts = dict()
        for word in strs:
            letterCount = [0] * 26
            for letter in word:
                letterCount[ord(letter) - ord('a')] += 1
            if tuple(letterCount) in letterCounts.keys():
                letterCounts[tuple(letterCount)].append(word)
            else:
                letterCounts[tuple(letterCount)] = [word]
        return letterCounts.values()
