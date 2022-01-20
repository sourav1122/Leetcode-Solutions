class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d={}
        p=0
        s=s.split(" ")
        #print(s)
        for i in s:
            if i not in d:
                d[i]=p
                p+=1
        #print(d,"jaaaa")
        fs=""
        for i in s:
            fs+=str(d[i])
        d2={}
        p=0
        for i in pattern:
            if i not in d2:
                d2[i]=p
                p+=1
        tcfs=""
        for i in pattern:
            tcfs+=str(d2[i])    
        #print(fs,tcfs)
        if fs==tcfs:
            return 1
        return 0
            
                