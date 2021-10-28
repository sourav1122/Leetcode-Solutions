class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i=0
        ans=set()
        arr=nums
        arr.sort()
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while(j<k):
                #print(i,j,k)
                if arr[i]+arr[j]+arr[k]==0:
                    #print("yuuuu")
                    ans.add((arr[i],arr[j],arr[k]))
                    j+=1
                elif arr[i]+arr[j]+arr[k]<0:
                    j+=1
                else:
                    k-=1
        ans=list(ans)
        return ans
            