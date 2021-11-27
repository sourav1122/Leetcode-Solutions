class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        mult=1
        zero=0
        for i in range(len(nums)):
            if nums[i]!=0:
                mult*=nums[i]
            else:
                zero+=1
        for i in range(len(nums)):
            if zero>=2:
                ans.append(0)
            elif zero==1 and nums[i]!=0:
                ans.append(0)
            elif nums[i]!=0:
                ans.append(mult//nums[i])
            else:
                ans.append(mult)
        return ans