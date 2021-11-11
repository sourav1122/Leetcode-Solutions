class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        mini=0
        nmini=99999999
        
        for i in range(len(nums)):
            nmini=min(nmini,mini+nums[i])
            mini+=nums[i]
            #print(mini)
        if nmini>0:
            return 1
        return abs(nmini)+1