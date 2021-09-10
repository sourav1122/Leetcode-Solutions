class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp=[0]*(len(nums))
        if len(nums)<=2:
            return 0
        dp[0]=0
        dp[1]=0
        for i in range(2,len(dp)):
            if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
                dp[i]=dp[i-1]+1
        return sum(dp)