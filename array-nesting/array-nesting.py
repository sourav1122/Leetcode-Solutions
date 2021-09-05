class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res=0
        vis=[0]*len(nums)
        for  i in range(len(nums)):
            if vis[i]!=1:
                st=nums[i]
                ct=0
                for j in range(len(nums)):
                    st=nums[st]
                    ct+=1
                    vis[st]=1
                    if st!=nums[i]:
                         res=max(res,ct)
                    #print(ct,"STTTTTTT")
                    else:
                        break
        return res+1