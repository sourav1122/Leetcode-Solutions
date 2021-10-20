class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans=0
        r=len(nums)
        nums.append(0)
        for i in range(r+1):
            ans=ans^i^nums[i]
        return ans
        