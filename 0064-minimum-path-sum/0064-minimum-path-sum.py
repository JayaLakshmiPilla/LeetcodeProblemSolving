class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ansGrid = [[float('inf')]*n for _ in range(m)]
        for i in range(m) :
            for j in range(n) :
                if i==0 and j==0 :
                    ansGrid[i][j] = grid[i][j]
                elif i==0 :
                    ansGrid[0][j] = grid[0][j] + ansGrid[0][j-1]
                elif j==0 :
                    ansGrid[i][0] = grid[i][0] + ansGrid[i-1][0]
                else :
                    ansGrid[i][j] = min(grid[i][j] + ansGrid[i][j-1],grid[i][j] + ansGrid[i-1][j])
        return ansGrid[m-1][n-1]
