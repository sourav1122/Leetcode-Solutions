class Solution:
    def groupAnagrams(self, strs):
        d={}
        for i in strs:
            x=sorted(i)
            x="".join(x)
            if x not in d:
                d[x]=[]
                d[x].append(i)
            else:
                d[x].append(i)
        ans=[]
        for i in d:
            ans.append(d[i])
        return ans
        
        
            
            
            
            
            
        