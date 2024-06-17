# Source: https://leetcode.com/problems/string-to-integer-atoi/

# Problem: String to Integer (atoi)

# Questions: 

# 1. Can a string have more than a sign? 
# 2. What if a letter is found after/before the number? 

class Solution:
    def myAtoi(self, s: str) -> int:
        number = 0
        sign = 1
        startedReading = False
        digits = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        allowed = set(['+', '-', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        for charac in s:
            if charac not in allowed:
                return self.round(number * sign)
            elif startedReading and charac not in digits:
                return self.round(number * sign)
            elif charac == '-':
                sign = -1
                startedReading = True
            elif charac == '+':
                sign = 1
                startedReading = True
            elif charac != ' ':
                number *= 10
                number += int(charac)
                startedReading = True
        return self.round(number * sign)
    
    def round(self, number: int) -> int:
        if number > (2**31 - 1):
            return 2**31 - 1
        elif number < -(2**31):
            return -(2**31)
        else:
            return number