class Solution:
    def arrangeCoins(self, n: int) -> int:
        f=1
        st=0
        
        while(n>0):
            #print(n)
            n-=f
            f+=1
            st+=1
        if n==0:
            return st
        else:
            return st-1
            