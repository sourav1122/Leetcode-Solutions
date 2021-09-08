class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        r=sum(nums)//2
        if sum(nums)%2!=0:
            return 0
        d=[[0 for i in range(r+1)]for j in range(len(nums)+1)]
        for i in range(len(d[0])):
            d[0][i]=0
        for i in range(len(d)):
            d[i][0]=1
        for i in range(1,len(d)):
            for j in range(1,len(d[0])):
                if j>=nums[i-1]:
                    d[i][j]=d[i-1][j] or d[i-1][j-nums[i-1]]
                else:
                    d[i][j]=d[i-1][j]
        #print(d)
        return d[len(nums)][r]