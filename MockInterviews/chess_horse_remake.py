"""
Given a chess horse with initial position in a NxN grid find all possible movements the horse can make.
The horse can move in any direction in L shape until reach the grid border.

If there is a piece in the square (cell cell is equal to 1), the movement is blocked.

x = linha
y = coluna

 Example:

Input:
Grid = [ 0 0 0 0 ]
       [ 0 0 0 0 ]
       [ 0 H 0 0 ]
       [ 0 0 0 0 ]
Position = 2, 1

Ouput: 3
"""

from typing import List


def horseMoves(position: List[int], grid: List[List[int]]) -> List[int]:
    possible_moves = [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [-1, -2], [1, -2]]
    result = []

    rows = len(grid)
    cols = len(grid[0])

    for move_row, move_col in possible_moves:
        new_row = position[0] + move_row
        new_col = position[1] + move_col
        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != 1:
            result.append([new_row, new_col])
    return result
