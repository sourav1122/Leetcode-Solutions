class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def isValid(x,y):
            if x<0 or x>=len(board) or y<0 or y>=len(board[0]):
                return 0
            return 1
        def isvisited(x,y):
            if vis[x][y]==1:
                return 0
            return 1
        def dfs(board,vis,x,y):
            if isValid(x,y+1):
                if isvisited(x,y+1) and board[x][y+1]=="O":
                    board[x][y+1]="A"
                    vis[x][y+1]=1
                    dfs(board,vis,x,y+1)
            if isValid(x+1,y):
                if isvisited(x+1,y) and board[x+1][y]=="O":
                    board[x+1][y]="A"
                    vis[x+1][y]=1
                    dfs(board,vis,x+1,y)
            if isValid(x-1,y):
                if isvisited(x-1,y) and board[x-1][y]=="O":
                    board[x-1][y]="A"
                    vis[x-1][y]=1
                    dfs(board,vis,x-1,y)
            if isValid(x,y-1):
                if isvisited(x,y-1) and board[x][y-1]=="O":
                    board[x][y-1]="A"
                    vis[x][y-1]=1
                    dfs(board,vis,x,y-1)
            return 
            
        vis=[[0 for i in range(len(board[0]))]for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i==0 or j==0 or i==len(board)-1 or j==len(board[0])-1) and board[i][j]=="O":
                    print(i,j)
                    dfs(board,vis,i,j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i!=0 and j!=0 and i!=len(board)-1 and j!=len(board[0])-1 and board[i][j]!="A":
                    board[i][j]="X"
                if board[i][j]=="A":
                    board[i][j]="O"
        
        """
        Do not return anything, modify board in-place instead.
        """
        