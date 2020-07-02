class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def solve(ans,n,k):
                if n==1:
                    ans+=str(digit[0])
                    return ans
                index=int(k/fact[n-1])
                if (k%fact[n-1])==0:
                     index-=1
                ans+=str(digit[index])
                del digit[index]
                k-=(fact[n-1]*(index))
                return solve(ans,n-1,k)
        fact=[1]
        f=1
        for i in range(1,n+1):
            f*=i
            fact.append(f)
        digit=[]
        for i in range(1,n+1):
            digit.append(i)
        ans=""
        return solve(ans,n,k)
            
