class Solution:
    def grayCode(self, n: int) -> List[int]:
        def gc(n):
            #print(n)
            if n==1:
                return ['0','1']
            x=gc(n-1)
            f=len(x)
            g=x[::-1]
            ans=[]
            for i in range(f):
                ans.append('0'+x[i])
            for i in range(f):
                ans.append('1'+g[i])
            
            return ans       
        anse=gc(n)
        for i in range(len(anse)):
            x=anse[i]
            x=int(x,2)
            anse[i]=x
        return anse
        