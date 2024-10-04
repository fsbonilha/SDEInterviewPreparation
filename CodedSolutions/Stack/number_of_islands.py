# Problem: Number of Islands

# Source : https://leetcode.com/problems/number-of-islands/

# Solution: Used a Breadth-First-Search - BFS Algorithm to mark all visited cells,
# a new island is counted when a not visited cell is found, since BFS marks all
# visited cells before proceding with the iteration.

import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def bfs(row, col):

            moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            queue = collections.deque()
            visited.add((row, col))
            queue.append((row, col))

            while queue:
                row, col = queue.popleft()
                for move_row, move_col in moves:
                    new_row, new_col = row + move_row, col + move_col

                    if (
                        new_row in range(rows) and
                        new_col in range(cols) and
                        grid[new_row][new_col] == "1" and
                        (new_row, new_col) not in visited
                    ):

                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1
        return islands
