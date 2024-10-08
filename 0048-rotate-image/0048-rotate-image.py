class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix) 
        for i in range(n//2) :
            
            matrix[i],matrix[n-i-1] = matrix[n-i-1],matrix[i]
            
        
        for i in range(n): 
            for j in range(i+1,n): 
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        return matrix        