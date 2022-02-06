class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()
        i=1
        while(i<=len(nums)-2):
            if nums[i]==nums[i-1]  and nums[i]==nums[i+1]:
                nums.pop(i+1)
                continue
            i+=1
        
            
                
            
        