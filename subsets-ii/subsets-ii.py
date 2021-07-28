class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        vis=[0]*(len(nums))
        def dfs(nums,vis,f,pos):
            ans.append(f)
            for i in range(len(nums)):
                if vis[i]!=1:
                    vis[i]=1
                    if i>=pos:
                        dfs(nums,vis,f+[nums[i]],i)
                    vis[i]=0
        dfs(nums,vis,[],0)
        fans=[]
        for i in ans:
            if i not in fans:
                fans.append(i)
        return fans