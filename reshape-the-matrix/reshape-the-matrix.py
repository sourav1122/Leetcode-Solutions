class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        f=[]
        if len(mat)*len(mat[0])!=r*c:
            return mat
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                 f.append(mat[i][j])
        f=f[::-1]
        ans=[[0 for i in range(c)]for j in range(r)]
        for i in range(r):
            for j in range(c):
                ans[i][j]=f[-1]
                f.pop(-1)
        return ans