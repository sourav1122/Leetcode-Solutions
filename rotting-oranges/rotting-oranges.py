class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=[]
        fresh=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append([i,j])
                if grid[i][j]==1:
                    fresh+=1
        def isValid(x,y):
            if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]):
                return 0
            else:
                return 1
        dex=[0,0,-1,1]
        dey=[-1,1,0,0]
        t=0
        if fresh==0:
            return 0
        while(q):
            curr=len(q)
            print(q)
            while(curr):
                x1,y1=q.pop(0)
                for i in range(4):
                    if isValid(x1+dex[i],y1+dey[i]):
                        if grid[x1+dex[i]][y1+dey[i]]==1:
                            grid[x1+dex[i]][y1+dey[i]]=2
                            q.append([x1+dex[i],y1+dey[i]])
                            fresh-=1
                
                curr-=1
            t+=1
            if fresh==0:
                break
        if fresh==0:
            return t
        else:
            return -1
                
            
                
        
        