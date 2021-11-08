class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nge=0
        for i in nums:
            nge^=i
        #print(nge)
        lsb=nge&(~(nge-1))
        result=[0,0]
        for i in nums:
            if lsb&i==0:
                result[0]^=i
            else:
                result[1]^=i
        return result