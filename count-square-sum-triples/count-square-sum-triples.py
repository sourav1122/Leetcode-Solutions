class Solution:
    def countTriples(self, n: int) -> int:
        d={}
        ans=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                if math.ceil(sqrt(i*i+j*j))==math.floor(sqrt(i*i+j*j)) and sqrt(i*i+j*j)<=n:
                    #print(i*i+j*j)
                    ans+=1
        return ans
        