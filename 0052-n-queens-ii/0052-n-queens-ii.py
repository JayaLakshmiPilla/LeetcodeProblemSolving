class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row):
            nonlocal count
            if row == n:
                count += 1
                return
            
            for col in range(n):
                if col in cols or (row - col) in neg_diags or (row + col) in pos_diags:
                    continue

                cols.add(col)
                neg_diags.add(row - col)
                pos_diags.add(row + col)

                backtrack(row + 1)

                cols.remove(col)
                neg_diags.remove(row - col)
                pos_diags.remove(row + col)

        count = 0
        cols = set()
        neg_diags = set()
        pos_diags = set()
        backtrack(0)
        return count
