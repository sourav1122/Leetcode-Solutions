class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[0]*(len(nums))
        dp[0]=1
        for i in range(1,len(nums)):
            maxi=0
            for j in range(i):
                if nums[j]<nums[i]:
                    if dp[j]>maxi:
                        maxi=dp[j]
            dp[i]=maxi+1
        return max(dp)
                