class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        c=0
        n=len(nums)
        nums.sort()
        for i in range(n-1,0,-1):
            l=0
            r=i-1
            while(l<r):
                if (nums[l]+nums[r]>nums[i]):
                    c+=(r-l)
                    r-=1
                else:
                    l+=1
        return c
        