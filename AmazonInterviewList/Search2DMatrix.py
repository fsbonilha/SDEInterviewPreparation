# Problem: Search 2D Matrix

# Source: https://neetcode.io/problems/search-2d-matrix

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        left = 0
        right = ROWS - 1
        while left <= right:
            row = left + (right - left) // 2
            if target > matrix[row][-1]:
                left = row + 1
            elif target < matrix[row][0]:
                right = row - 1
            else:
                break

        if left > right:
            return False

        left = 0
        right = COLS - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
        return False
