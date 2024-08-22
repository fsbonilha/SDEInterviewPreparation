# Problem: Evaluate Reverse Polish Notation

# Source: https://neetcode.io/problems/evaluate-reverse-polish-notation


from collections import deque
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        numDeque = deque()

        for token in tokens:
            if token not in operators:
                numDeque.append(int(token))
            else:
                second = int(numDeque.pop())
                first = int(numDeque.pop())

                if token == "+":
                    result = first + second
                elif token == "-":
                    result = first - second
                elif token == "*":
                    result = first * second
                elif token == "/":
                    result = int(first / second)
                numDeque.append(result)
        return numDeque.pop()
