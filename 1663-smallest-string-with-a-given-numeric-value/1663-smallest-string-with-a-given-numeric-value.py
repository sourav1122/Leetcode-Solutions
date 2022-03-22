class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        fs=[1]*(n)
        k-=n
        j=n-1
        while(k>0):
            if k>=25:
                fs[j]+=25
                j-=1
                k-=25
            else:
                fs[j]+=k
                k=0
                j-=1
        fss=""
        for i in fs:
            fss+=chr(i+ord('a')-1)
        return fss
            
        