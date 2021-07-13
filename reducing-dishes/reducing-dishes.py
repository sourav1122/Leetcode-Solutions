class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        x=satisfaction
        p=len(x)
        ans=0
        for i in range(p):
            #print(i)
            
            maxi=0
            #print(x)
            for j in range(len(x)):
                maxi+=(j+1)*x[j]
                
            ans=max(ans,maxi)
            x=x[1:p]
        return ans
                