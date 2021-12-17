class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict
        adj=defaultdict(list)
        if n==1:
            return [0]
        deg=[0]*(n)
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
            deg[i[0]]+=1
            deg[i[1]]+=1
        q=[]
        for i in range(n):
            if deg[i]==1:
                q.append(i)
        count=n
        while(count>2):
            lent=len(q)
            count-=lent
            while(lent):
                x=q.pop(0)
                for j in adj[x]:
                    deg[j]-=1
                    if deg[j]==1:
                        q.append(j)
                lent-=1
            
        return q
            