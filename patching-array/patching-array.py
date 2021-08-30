class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i=0
        reach=0
        cnt=0
        while(reach<n):
            if i>=len(nums):
                reach=2*reach+1
                cnt+=1
            elif i<len(nums) and nums[i]<=reach+1:
                reach+=nums[i]
                i+=1
            else:
                reach=2*reach+1
                cnt+=1
        return cnt
            