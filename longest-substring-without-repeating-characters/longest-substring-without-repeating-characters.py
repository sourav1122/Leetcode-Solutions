class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #r=list(set(s))
        d={}
        
        maxi=0
        ap=0
        bp=0
        while(bp<len(s)):
            #print(d)
            if s[bp] not in d:
                d[s[bp]]=0
                bp+=1
                maxi=max(len(d),maxi)
            else:
                del d[s[ap]]
                ap+=1
        return maxi
                
                
                
                
            
            
        