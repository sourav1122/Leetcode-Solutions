class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        rank=0
        direct=[[0 for i in range(n)]for j in range(n)]
        count=[0]*(n)
        for i in roads:
            x,y=i
            count[x]+=1
            count[y]+=1
            direct[x][y]=1
            direct[y][x]=1
        
        for i in range(n):
            for j in range(i+1,n):
                rank=max(rank,count[i]+count[j]-direct[i][j])
        return rank