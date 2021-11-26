class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_till_now=-9999999
        sumi=0
        for i in range(len(nums)):
            sumi+=nums[i]
            #print(sumi,max_till_now)
            if sumi>max_till_now:
                max_till_now=sumi
            if sumi<0:
                sumi=0
        return max_till_now