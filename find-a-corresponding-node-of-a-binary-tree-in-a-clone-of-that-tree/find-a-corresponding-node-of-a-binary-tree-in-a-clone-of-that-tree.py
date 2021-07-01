# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(r,valu,ans):
            if r==None:
                return ans
            if r.val==valu:
                return r
            ans=dfs(r.left,valu,ans)
            ans=dfs(r.right,valu,ans)
            return ans
        
        ans=dfs(cloned,target.val,None)
        return ans