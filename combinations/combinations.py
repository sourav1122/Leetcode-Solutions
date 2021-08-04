class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        p=[]
        vis=[0]*n
        for i in range(1,n+1):
            p.append(i)
        r=[]
        def dfs(arr,vis):
            #print(arr)
            if len(arr)==k:
                r.append(arr)
                return
            for i in range(n):
                if vis[i]!=1:
                    vis[i]=1
                    if len(arr)>=1:
                        if p[i]>arr[-1]:
                            dfs(arr+[p[i]],vis)
                    if len(arr)==0:
                        dfs(arr+[p[i]],vis)
                    vis[i]=0
        dfs([],vis)
        return r
                    
        
            