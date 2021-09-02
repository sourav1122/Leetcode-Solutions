class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
            V=len(graph)
            adj=graph
            vis=[0 for i in range(V)]
            colour=[0 for i in range(V)]
            def dfs(v,color,vis,ans,colour):
                colour[v]=color
                vis[v]=1
                for i in adj[v]:
                    if vis[i]==0:
                        if colour[v]==1:
                            ans=dfs(i,0,vis,ans,colour)
                        else:
                            ans=dfs(i,1,vis,ans,colour)
                    else:
                        if colour[i]==colour[v]:
                            ans=0
                            return ans
                return ans
            for i in range(V):
                if vis[i]!=1:
                    ans=dfs(i,0,vis,1,colour)
                    if ans==0:
                        return 0
            return ans            
                            
                    
                    
  