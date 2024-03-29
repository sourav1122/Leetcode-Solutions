# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lo=1
        hi=n
        while(lo<=hi):
            mid=(lo+hi)//2
            r=guess(mid)
            #print(mid,r)
            if r==0:
                return mid
            elif r==1:
                lo=mid+1
            else:
                hi=mid-1
        return -1