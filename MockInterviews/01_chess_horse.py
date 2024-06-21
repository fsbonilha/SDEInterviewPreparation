"""
Given a chess horse with initial position in a NxN grid find all possible movements the horse can make. 
The horse can move in any direction in L shape until reach the grid border.

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

class Solution:
    const POSSIBLE_MOVES = [
        # UP - Left
        [(-1, 0), (-1, 0), (0, -1)],
        # Up - Right
        [(-1, 0), (-1, 0), (0, 1)],
        # Right - Up
        [(0, 1), (0, 1), (-1, 0)],
        # Right - Down
        [(0, 1), (0, 1), (1, 0)],
    ]
    
    def find_horse_moves(self, grid: List(List), pos: Tuple(int, int)):
        moves = 0
        
        for possible_move in POSSIBLE_MOVES:
            if self.is_valid_move(grid, current_pos, pos.copy()):
                moves++
            
        return moves
        
    def is_valid_move(self, grid, current_post, possible_move):
        is_valid_move = True
        
        for move in possible_move:
            current_pos[0] += move[0]
            current_pos[1] += move[1]
            if is_valid_position(grid, current_pos):
                is_valid_move = False
                break;
                
        return is_valid_move
        
    def is_valid_position(self, grid, current_pos):
        return current_pos[0] < 0 
            or current_pos[0] >= len(grid) 
            or current_pos[1] < 0 
            or current_pos[1] >= len(grid[0]) 
            or grid[current_pos[0], current_pos[1]] == 1          
