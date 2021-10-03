class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=-9999999
        cur_max=0
        for i in range(len(nums)):
            cur_max+=nums[i]
            if cur_max>maxi:
                maxi=max(maxi,cur_max)
            if cur_max<0:
                cur_max=0
        return maxi