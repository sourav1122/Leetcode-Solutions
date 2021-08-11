class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        q=[]
        M=grid
        m=len(grid)
        n=len(grid[0])
        def isvalid(sx,sy):
            if sx<0 or sx>=m or sy<0 or sy>=n:
                return 0
            return 1
        dex=[-1,0,1,0]
        dey=[0,1,0,-1]
        fans=0
        def dfs(sx,sy,ans,vis):
            nonlocal fans
            fans=max(fans,ans)
            for i in range(4):
                if isvalid(sx+dex[i],sy+dey[i]) and vis[sx+dex[i]][sy+dey[i]]!=1 and M[sx+dex[i]][sy+dey[i]]!=0:
                    vis[sx+dex[i]][sy+dey[i]]=1
                    dfs(sx+dex[i],sy+dey[i],ans+M[sx+dex[i]][sy+dey[i]],vis)
                    vis[sx+dex[i]][sy+dey[i]]=0

        for i in range(m):
            for j in range(n):
                vis=[[0 for i in range(n)]for j in range(m)]
                vis[i][j]=1
                dfs(i,j,M[i][j],vis)
                #print(fans)
                
                
        return fans        