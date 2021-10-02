class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m=len(dungeon)
        n=len(dungeon[0])
        maxi=99999999
        dp=[[-1 for i in range(n)]for j in range(m)]
        def rec(i,j,dungeon):
            if i>=m or j>=n:
                return maxi
            if dp[i][j]!=-1:
                return dp[i][j]
            health=min(rec(i+1,j,dungeon),rec(i,j+1,dungeon))
            if health==maxi:
                health=1
            dp[i][j]=0
            if health-dungeon[i][j]>0:
                dp[i][j]=health-dungeon[i][j]
            else:
                dp[i][j]=1
            return dp[i][j]
        return rec(0,0,dungeon)
        
        