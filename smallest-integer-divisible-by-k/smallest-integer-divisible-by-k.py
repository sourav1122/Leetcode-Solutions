class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2==0 and k%5==0:
            return -1
        rem=0
        for i in range(1,k+1):
            rem=(rem*10+1)%k
            if rem==0:
                return i
        return -1
            