class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if sum(nums)==0:
            return 0
        na=[0]*(100000)
        for i in range(len(nums)):
            na[nums[i]]+=nums[i]
        #print(na[:6])
        dp=[-1]*(100000)
        def sumi(indi):
            if indi<0:
                return 0
            if dp[indi]!=-1:
                return dp[indi]
            #print(f1,f2)
            dp[indi]=max(sumi(indi-2)+na[indi],sumi(indi-1))
            return dp[indi]
        #print(dp[:6])
        return sumi(len(na)-1)
        #return dp[-1]        