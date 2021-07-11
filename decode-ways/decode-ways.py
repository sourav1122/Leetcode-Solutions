class Solution:
    def numDecodings(self, s: str) -> int:
        dp=[0]*(len(s))
        if s=="":
            return 0
        if s[0]=='0':
            dp[0]=0
        else:
            dp[0]=1
        for i in range(1,len(s)):
            #print(i)
            s1=int(s[i:i+1])
            s2=int(s[i-1:i+1])
            #print(s1,s2)
            if 1<=s1<=9:
                dp[i]+=dp[i-1]
            if 10<=s2<=26:
                if i>=2:
                    dp[i]+=dp[i-2]
                else:
                    dp[i]+=1
        return dp[len(s)-1]
            
         