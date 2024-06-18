# Source: https://leetcode.com/problems/valid-parentheses/

# Problem: 07.ValidParenthesis

# Questions: 
# 1. Do we have another characters besides {}()[] ?

# Complexity O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'{': '}', '(': ')', '[': ']'}
        index = 0
        for charac in s:
            if charac in pairs.keys():
                stack.append(charac)
            elif len(stack) <= 0:
                return False
            elif charac != pairs[stack.pop()]:
                return False
        if len(stack) == 0:
            return True
        return False

        
        