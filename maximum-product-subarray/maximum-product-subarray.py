class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxend=nums[0]
        globsum=nums[0]
        minend=nums[0]
        for i in range(1,len(nums)):
            tmp=maxend
            maxend=max(nums[i],maxend*nums[i],minend*nums[i])
            minend=min(nums[i],tmp*nums[i],minend*nums[i])
            globsum=max(globsum,maxend)
        return globsum
            