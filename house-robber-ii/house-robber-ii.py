class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        dp=[-1]*(len(nums))
        def k(pos,arr):
            if pos<0:
                return 0
            if dp[pos]!=-1:
                return dp[pos]
            dp[pos]= max(arr[pos]+k(pos-2,arr),k(pos-1,arr))
            return dp[pos]
        f1=k(len(nums)-2,nums[1:])
        dp=[-1]*(len(nums))
        f2=k(len(nums)-2,nums[:len(nums)-1])
        return max(f1,f2)