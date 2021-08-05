class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if sum(cost)==0:
            return 0
        a=cost
        dp=[0]*(len(a))
        dp[0]=a[0]
        dp[1]=a[1]
        for i in range(2,len(a)):
            dp[i]=a[i]+min(dp[i-1],dp[i-2])
        return min(dp[len(a)-1],dp[len(a)-2])
        