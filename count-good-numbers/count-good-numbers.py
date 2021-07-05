class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def power(x, y):
                if(y == 0): return 1
                temp = power(x, int(y / 2))
                if (y % 2 == 0):
                     return (temp * temp)%1000000007
                else:
                    if(y > 0): return (x * temp * temp)%1000000007
                    else: return ((temp * temp) / x)%1000000007
        if n%2!=0:
            #print("haa")
            ans=power(5,(n//2)+1)
            ans1=power(4,(n//2))
            return (ans*ans1)%1000000007
        else:
            ans=power(5,(n//2))
            ans1=power(4,(n//2))
            return (ans*ans1)%1000000007
            