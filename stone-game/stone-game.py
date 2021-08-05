class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        st=0
        end=len(piles)-1
        dp=[[0 for i in range(len(piles))]for j in range(len(piles))]
        def solve(st,end):
            if st>end:
                return 0
            if st==end:
                return piles[st]
            if dp[st][end]!=0:
                return dp[st][end]
            dp[st][end]=max(piles[st]+solve(st+1,end),piles[end]+solve(st,end-1))
            return dp[st][end]
        x=solve(st,end)
        return x