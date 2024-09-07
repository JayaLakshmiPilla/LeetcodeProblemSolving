from queue import deque 
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix) 
        n = len(matrix[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0 :
                    q.append((i,j)) 
        while(q) :
            i,j = q.popleft()
            for k in range(n) : 
                matrix[i][k] = 0 
            for k in range(m) : 
                matrix[k][j] = 0



        
        