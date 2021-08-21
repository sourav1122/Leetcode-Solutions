class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set()
        for i in nums:
            s.add(i)
        cs=0
        ls=0
        for i in range(len(nums)):
            if nums[i]-1 not in s:
                curr_num=nums[i]
                cs=1
                while(curr_num+1 in s):
                    curr_num+=1
                    cs+=1
                ls=max(ls,cs)
        return ls
                    
                