# Problem: Minimum Window with Characters

# Source: https://neetcode.io/problems/minimum-window-with-characters

# Complexity: O(N)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for letter in t:
            countT[letter] = 1 + countT.get(letter, 0)

        have, need = 0, len(countT)
        resultLen = float("infinity")
        resultL, resultR = 0, 0

        left = 0
        for right in range(len(s)):
            letter = s[right]
            window[letter] = 1 + window.get(letter, 0)
            if letter in countT and window[letter] == countT[letter]:
                have += 1

            while have == need:
                if (right - left + 1) < resultLen:
                    resultL = left
                    resultR = right
                    resultLen = right - left + 1

                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        return s[resultL:resultR + 1] if resultLen != float("infinity") else ""
