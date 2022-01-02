class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d={}
        c=0
        for i in range(len(time)):
            f=0
            for j in d:
                if (time[i]+j)%60==0:
                        f=1
                        c+=d[j]
            if time[i] not in d:
                    d[time[i]]=1
            else:
                    d[time[i]]+=1
        return c
        