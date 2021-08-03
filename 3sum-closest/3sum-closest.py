class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res=[]
        diff=99999999
        nums.sort()
        for i in range(len(nums)):
            l,r=i+1,len(nums)-1
            while(l<r):
                ts=nums[i]+nums[l]+nums[r]
                #print(ts,target-ts)
                if abs(target-ts)<= abs(diff):
                    diff=target-ts
                if ts<target:
                    l+=1
                else:
                    r-=1
                #print(diff)
            
        return target-diff