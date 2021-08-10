class Solution:
    def hammingWeight(self, n: int) -> int:
        n=bin(n)
        n=n[2:]
        count=0
        for i in range(len(n)):
            #print(n[i])
            if int(n[i]) & 1==1:
                count+=1
        return count
            
        