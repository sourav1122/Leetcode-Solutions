class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        val=0
        ans=""
        for i in range(len(s)-1,-1,-1):
            val+=shifts[i]
            val=val%26
            nval=val
            if val>=26-(ord(s[i])-ord('a')):
                f=26-(ord(s[i])-ord('a'))-1
                #print(f,"YAHA",s[i])
                nval-=f
                ans=chr(nval+96)+ans
            else:
                #print(s[i],val)
                f=ord(s[i])+val
                ans=chr(f)+ans
        return ans