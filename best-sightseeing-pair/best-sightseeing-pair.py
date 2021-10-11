class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_so_far=values[0]+0
        res=0
        for i in range(1,len(values)):
            res=max(res,max_so_far+values[i]-i)
            max_so_far=max(max_so_far,values[i]+i)
        return res
            
            