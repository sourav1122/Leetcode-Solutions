class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        def isvalid(sx,sy):
            if sx<0 or sx>=m or sy<0 or sy>=n:
                return 0
            return 1
        vis=[[0 for i in range(len(board[0]))]for j in range(len(board))]
        dex=[-1,0,1,0]
        dey=[0,1,0,-1]
        def dfs(sx,sy,ans,vis,f,ind):
            #print(ans)
            if ans==word:
                return 1
            for i in range(4):
                if isvalid(sx+dex[i],sy+dey[i]) and vis[sx+dex[i]][sy+dey[i]]!=1 and board[sx+dex[i]][sy+dey[i]]==word[ind]:
                    vis[sx+dex[i]][sy+dey[i]]=1
                    f=dfs(sx+dex[i],sy+dey[i],ans+board[sx+dex[i]][sy+dey[i]],vis,f,ind+1)
                    vis[sx+dex[i]][sy+dey[i]]=0
            return f
        for i in range(len(board)):
            for j in range(len(board[0])):
                f=0
                vis=[[0 for i in range(len(board[0]))]for j in range(len(board))]
                if board[i][j]==word[0] :
                    #print(board[i][j],word[0],"klkll")
                    vis[i][j]=1
                    ans=board[i][j]
                    ind=0
                    f=dfs(i,j,ans,vis,0,ind+1)
                    if f==1:
                        return 1
        return 0
            
                
            