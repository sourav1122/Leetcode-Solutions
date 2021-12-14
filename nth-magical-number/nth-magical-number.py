class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        l=min(a,b)
        r=l*n
        lcm=(a*b)//math.gcd(a,b)
        while(l<r):
            mid=(l+(r-l)//2)
            factor=(mid//a)+(mid//b)-(mid//lcm)
            if factor<n:
                l=mid+1
            else:
                r=mid
        mod=(10**9)+7
        return l%mod