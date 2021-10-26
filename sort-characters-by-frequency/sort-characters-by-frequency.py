class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        v=[]
        for i in d:
            v.append([i,d[i]])
        v.sort(reverse=True ,key = lambda x: x[1] )
        ans=""
        for i in v:
            ans+=i[0]*i[1]
        return ans
        
        