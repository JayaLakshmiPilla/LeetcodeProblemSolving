from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def backtrack(r, c, index):
            if index == len(word):
                return True  # All characters matched
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return False
            if board[r][c] != word[index]:
                return False

            temp = board[r][c]
            board[r][c] = '#'  # Mark as visited
            
            # Explore all 4 directions: up, down, left, right
            found = (backtrack(r+1, c, index+1) or
                     backtrack(r-1, c, index+1) or
                     backtrack(r, c+1, index+1) or
                     backtrack(r, c-1, index+1))
            
            board[r][c] = temp  # Unmark (backtrack)
            return found

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and backtrack(i, j, 0):
                    return True
        return False
