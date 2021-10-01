class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        pos1=len(text1)
        pos2=len(text2)
        dp=[[-1 for i in range(pos2)]for j in range(pos1)]
        def k(pos1,pos2):
            if pos1<0 or pos2<0:
                return 0
            if dp[pos1][pos2]!=-1:
                return dp[pos1][pos2]
            if text1[pos1]==text2[pos2]:
                dp[pos1][pos2]= 1+k(pos1-1,pos2-1)
                return dp[pos1][pos2]
            dp[pos1][pos2]= max(k(pos1-1,pos2),k(pos1,pos2-1))
            return dp[pos1][pos2]
        k(pos1-1,pos2-1)
        return dp[-1][-1]
        