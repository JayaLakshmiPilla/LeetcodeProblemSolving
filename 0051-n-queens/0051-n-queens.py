from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row):
            if row == n:
                board = []
                for i in range(n):
                    line = ['.'] * n
                    line[queens[i]] = 'Q'
                    board.append("".join(line))
                res.append(board)
                return
            
            for col in range(n):
                if col in cols or (row - col) in neg_diagonals or (row + col) in pos_diagonals:
                    continue

                # Place queen
                queens[row] = col
                cols.add(col)
                neg_diagonals.add(row - col)
                pos_diagonals.add(row + col)

                backtrack(row + 1)

                # Remove queen
                cols.remove(col)
                neg_diagonals.remove(row - col)
                pos_diagonals.remove(row + col)

        res = []
        queens = [-1] * n  # index = row, value = col
        cols = set()
        neg_diagonals = set()
        pos_diagonals = set()
        backtrack(0)
        return res
