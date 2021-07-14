class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q=[]
        q.append([entrance[0],entrance[1],0])
        vis=[[0 for i in range(len(maze[0]))]for j in range(len(maze))]
        def isvalid(sx,sy):
            if sx<0 or sx>=len(maze) or sy<0 or sy>=len(maze[0]):
                return 0
            return 1
        dex=[-1,0,1,0]
        dey=[0,1,0,-1]
        ans=9999999999
        vis[entrance[0]][entrance[1]]=1
        while(q):
            f=len(q)
            #print(f)
            while(f):
                x=q.pop(0)
                #print(x)
                sx=x[0]
                sy=x[1]
                cost=x[2]
                if (sx==0 or sy==0 or sx==len(maze)-1 or sy==len(maze[0])-1) and (sx!=entrance[0] or sy!=entrance[1]):
                    ans=min(ans,cost)
                for i in range(4):
                    if isvalid(sx+dex[i],sy+dey[i]) and maze[sx+dex[i]][sy+dey[i]]=="." and vis[sx+dex[i]][sy+dey[i]]!=1:
                        q.append([sx+dex[i],sy+dey[i],cost+1])
                        vis[sx+dex[i]][sy+dey[i]]=1
                f-=1
        if ans==9999999999:
            return -1
        return ans
        
                    
            
            
        
                        
            
        