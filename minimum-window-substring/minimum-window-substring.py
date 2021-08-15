class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        window=[0]*123
        required=[0]*123
        for i in t:
            required[ord(i)]+=1
        for i in s:
            window[ord(i)]+=1
        for i in range(123):
            if window[i]<required[i]:
                return ""
        window=[0]*123
        l=0
        r=0
        ans=999999999
        st=0
        en=0
        window[ord(s[r])]+=1
        while(r<len(s) or l<len(s)):
            c=0
            for i in range(123):
                if required[i]<=window[i]:
                    continue
                else:
                    c=1
                    break
            if c!=1:
                if ans>r-l:
                    st=l
                    en=r
                    ans=min(ans,r-l)
            if c==0:
                if window[ord(s[l])]!=0:
                    window[ord(s[l])]-=1
                l+=1
            else:
                r+=1
                if l==r==len(s):
                    break
                if r>=len(s) and l<len(s): 
                    r-=1
                    window[ord(s[l])]-=1
                    l+=1
                else:
                    window[ord(s[r])]+=1

        #print(st,en)
        return s[st:en+1]
            
            