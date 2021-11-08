class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        dex=[-1,0,1,0]
        dey=[0,1,0,-1]
        m=len(grid)
        n=len(grid[0])
        def dfs(sx,sy,vis,ct):
            #print(sx,sy)
            global ans
            if grid[sx][sy]==2 and ct==m*n-ob:
                ans+=1
            for i in range(4):
                if 0<=sx+dex[i]<m and 0<=sy+dey[i]<n and vis[sx+dex[i]][sy+dey[i]]!=1 and grid[sx+dex[i]][sy+dey[i]]!=-1:
                    vis[sx+dex[i]][sy+dey[i]]=1
                    dfs(sx+dex[i],sy+dey[i],vis,ct+1)
                    vis[sx+dex[i]][sy+dey[i]]=0
        
        global ans
        ans=0
        vis=[[0 for i in range(n)]for j in range(m)]
        ob=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==-1:
                    ob+=1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    vis[i][j]=1
                    dfs(i,j,vis,1)
        return ans
                
                