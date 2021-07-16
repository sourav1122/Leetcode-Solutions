class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        s=set()
        #print(nums)
        for i in range(n-3):
            #print(i,"klk")
            for j in range(i+1,n-2):
                l=j+1
                r=n-1
                #print(i,j,l,r)
                while(l<r):
                    sumi=nums[i]+nums[j]+nums[l]+nums[r]
                    if sumi==target:
                        s.add((nums[i],nums[j],nums[l],nums[r]))
                    if sumi<=target:
                        l+=1
                    if sumi>target:
                        r-=1
        #print(s)

        ans=[]
        for i in s:
            p=list(i)
            ans.append(p)
        return ans
                        