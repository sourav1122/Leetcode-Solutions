class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)==1:
            return 1
        maxpoint=0
        for i in range(len(points)-1):
            slopes=dict()
            for j in range(i+1,len(points)):
                x1,y1=points[i]
                x2,y2=points[j]
                if x1!=x2:
                    slope=(y2-y1)/(x2-x1)
                else:
                    slope=float("inf")
                if slope not in slopes:
                    slopes[slope]=2
                else:
                    slopes[slope]+=1
            maxpoint=max(maxpoint,max(slopes.values()))
        if len(points)==1:
            return 1
        return maxpoint        