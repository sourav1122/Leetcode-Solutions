class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        r=sum(nums)//2
        if sum(nums)%2!=0:
            return 0
        d=[[-1 for i in range(r+1)]for j in range(len(nums)+1)]
        def k(nums,r,pos):
            if r==0:
                #print("HA")
                d[pos][r]=1
                return d[pos][r]
            if pos<0:
                return 0
            if d[pos][r]!=-1:
                return d[pos][r]
            if nums[pos]<=r:
                #print(k(nums,r-nums[pos-1],pos-1),k(nums,r,pos-1))
                d[pos][r]= k(nums,r-nums[pos-1],pos-1) or k(nums,r,pos-1)
                return d[pos][r]
            else:
                d[pos][r]= k(nums,r,pos-1)
                return d[pos][r]
        return k(nums,r,len(nums)-1)
                