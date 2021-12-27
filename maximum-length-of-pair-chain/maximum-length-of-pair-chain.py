class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[0])
        dp=[1]*(len(pairs))
        for i in range(1,len(pairs)):
            maxi=0
            for j in range(i):
                if pairs[j][1]<pairs[i][0]:
                    maxi=max(maxi,dp[j])
            dp[i]=maxi+1
        return max(dp)
        