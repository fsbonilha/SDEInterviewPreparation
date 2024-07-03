# Source:
# https://leetcode.com/problems/valid-sudoku/
# https://neetcode.io/problems/valid-sudoku

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        linSize = len(board)
        colSize = len(board[0])

        colMaps = [set() for _ in range(colSize)]
        linMaps = [set() for _ in range(linSize)]
        boxMaps = [[set() for _ in range(colSize//3)] for _ in range(linSize//3)]
        for indexLine, line in enumerate(board):
            for indexCol, num in enumerate(line):
                if num == ".":
                    continue
                indexBoxCol = indexCol//3
                indexBoxLine = indexLine//3
                if (num in colMaps[indexCol] or
                    num in linMaps[indexLine] or
                    num in boxMaps[indexBoxLine][indexBoxCol]):
                    return False
                colMaps[indexCol].add(num)
                linMaps[indexLine].add(num)
                boxMaps[indexBoxLine][indexBoxCol].add(num)
        return True
