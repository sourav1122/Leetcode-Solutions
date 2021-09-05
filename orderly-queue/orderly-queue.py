class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k==1:
            x=s
            for i in range(len(s)):
                #print(s[i:]+s[:i])
                x=min(x,s[i:]+s[:i])
                #print(x,"YAHAPE")
            return x
                
        else:
            return "".join(sorted(s))