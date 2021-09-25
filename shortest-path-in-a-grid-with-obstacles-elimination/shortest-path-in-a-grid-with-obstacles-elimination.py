class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m=len(grid)
        n=len(grid[0])
        def isvalid(sx,sy):
            if sx<0 or sx>=m or sy<0 or sy>=n:
                return 0
            return 1
        dex=[-1,0,1,0]
        dey=[0,1,0,-1]
        q = deque([(0, 0, 0, k)])
        vis=set()
        ans=999999999
        while(q):
            f=len(q)
            while(f):
                x1,y1,ct,nk=q.popleft()
                if (x1,y1,nk) in vis:
                    f-=1
                    continue
                if x1==m-1 and y1==n-1:
                    return ct
                vis.add((x1,y1,nk))
                for i in range(4):
                    if isvalid(x1+dex[i],y1+dey[i]) and grid[x1+dex[i]][y1+dey[i]]==0:
                        q.append((x1+dex[i],y1+dey[i],ct+1,nk))
                    elif isvalid(x1+dex[i],y1+dey[i]) and grid[x1+dex[i]][y1+dey[i]]==1:
                        if nk>0:
                            q.append((x1+dex[i],y1+dey[i],ct+1,nk-1))
                    
                f-=1
        return -1
                    
                
                
                
                