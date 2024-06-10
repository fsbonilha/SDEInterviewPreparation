class Solution:
    def romanToInt(self, s: str) -> int:
        letters = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        idx = 0
        result = 0
        while idx < (len(s) - 1):
            current_letter = s[idx]
            next_letter = s[idx + 1]
            if (letters[current_letter] >= letters[next_letter]):
                result += letters[current_letter]
            else:
                result -= letters[current_letter]
            idx += 1
        last_letter = s[len(s) - 1]
        result += letters[last_letter]
        return result
        
