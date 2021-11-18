class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        f=[]
        for i in range(len(nums)):
            if nums[abs(nums[i])-1]>0:
                nums[abs(nums[i])-1]=-nums[abs(nums[i])-1]
        #print(nums)
        for i in range(len(nums)):
            if nums[i]>0:
                f.append(i+1)
        return f
        