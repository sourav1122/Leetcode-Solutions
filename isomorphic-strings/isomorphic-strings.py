class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return 0
        d={}
        d1={}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=t[i]
            else:
                if d[s[i]]!=t[i]:
                    return 0
        for i in range(len(t)):
            if t[i] not in d1:
                d1[t[i]]=s[i]
            else:
                if d1[t[i]]!=s[i]:
                    return 0
        #print(d)
        return 1