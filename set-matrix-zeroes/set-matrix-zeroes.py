class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        vis=[ [ 0 for i in range(len(matrix[0])) ] for j in range(len(matrix)) ] 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    vis[i][j]=1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0 and vis[i][j]==1:
                    for k in range(len(matrix[0])):
                         matrix[i][k]=0
                    for f in range(len(matrix)):
                        matrix[f][j]=0
        
                        
        """
        Do not return anything, modify matrix in-place instead.
        """
        