class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        def isvalid(sx,sy):
            if sx<0 or sy<0 or sx>=m or sy>=n:
                return 0
            return 1
        dex=[-1,0,1,0]
        dey=[0,1,0,-1]
        vis=[[0 for i in range(n)]for j in range(m)]
        def dfs(sx,sy,count,ide):
            for i in range(4):
                if isvalid(sx+dex[i],sy+dey[i]) and grid[sx+dex[i]][sy+dey[i]]==1 and vis[sx+dex[i]][sy+dey[i]]!=1 :
                    vis[sx+dex[i]][sy+dey[i]]=1
                    grid[sx+dex[i]][sy+dey[i]]=ide
                    count=1+dfs(sx+dex[i],sy+dey[i],count,ide)
            return count
        from collections import defaultdict
        counte=defaultdict()
        counte[0]=0
        ide=2
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and vis[i][j]==0:
                    vis[i][j]=1
                    count= dfs(i,j,1,ide)
                    grid[i][j]=ide
                    counte[ide]=count
                    ide+=1
        if 2 not in counte:
            fans=0
        else:
            fans=counte[2]
        for i in range(m):
            for j in range(n):
                #print(i,j)
                if grid[i][j]==0:
                    area=1
                    s=set()
                    for k in range(4):
                        if isvalid(i+dex[k],j+dey[k]):
                            #print("haaa",s,grid[i+dex[k]][j+dey[k]])
                            s.add(grid[i+dex[k]][j+dey[k]])
                    #print(s)
                    for inde in s:
                        area+=counte[inde]
                    fans=max(fans,area)
        return fans
                        
                            
                            
                            
                        
        
        