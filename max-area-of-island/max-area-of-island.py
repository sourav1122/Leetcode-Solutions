class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def isvalid(sx,sy):
                if sx<0 or sx>=len(grid) or sy<0 or sy>=len(grid[0]):
                    return 0
                return 1
        dex =[-1,0,1,0]
        dey=[0,1,0,-1]
        def dfs(sx,sy,ans):
            vis[sx][sy]=1
            for i in range(4):
                if isvalid(sx+dex[i],sy+dey[i]) and vis[sx+dex[i]][sy+dey[i]]!=1 and grid[sx+dex[i]][sy+dey[i]]==1:
                     ans=dfs(sx+dex[i],sy+dey[i],ans+1)
            return ans 
        fans=0
        r,c=len(grid),len(grid[0])
        vis=[[0 for i in range(c)]for j in range(r)]
        for i in range(r):
             for j in range(c):
                    if grid[i][j]==1 and vis[i][j]!=1:
                        ans=1
                        ans=dfs(i,j,ans)
                        fans=max(ans,fans)
        return fans