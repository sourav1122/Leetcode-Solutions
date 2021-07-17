class Solution:
    def rob(self, nums: List[int]) -> int:
        if sum(nums)==0:
            return 0
        a=nums
        dp=[0]*(len(a))
        def sumi(indi):
            if indi<0:
                return 0
            if dp[indi]!=0:
                return dp[indi]
            #print(f1,f2)
            dp[indi]=max(sumi(indi-2)+a[indi],sumi(indi-1))
            return dp[indi]
        sumi(len(a)-1)
        return dp[-1]
            