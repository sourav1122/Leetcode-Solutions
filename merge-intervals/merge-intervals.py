class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        p=[]
        intervals=sorted(intervals)
        if len(intervals)==1 or len(intervals)==0:
            return intervals
        ans=[]
        p.append(intervals[0])
        for i in range(1,len(intervals)):
            #print(intervals[i])
            if intervals[i][0]<=p[-1][1]:
                p[-1]=[min(p[-1][0],intervals[i][0]),max(p[-1][1],intervals[i][1])]
            else:
                p.append(intervals[i])
        return p
            
            
        