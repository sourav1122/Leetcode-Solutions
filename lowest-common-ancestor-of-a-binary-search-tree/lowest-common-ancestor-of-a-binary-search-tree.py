# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p1=[]
        def dfs(r,ans,valu):
            nonlocal p1
            #print(ans)
            if r==None:
                return
            if r.val==valu:
                ans+=[r]
                p1+=[ans]
                #print(r.val,ans,"klklklklk")
                return 
            dfs(r.left,ans+[r],valu)
            dfs(r.right,ans+[r],valu)
        dfs(root,[],p.val)
        dfs(root,[],q.val)
        p2=p1[0]
        p3=p1[1]
        #print(p2,p3)
        ans=-1
        p2val=[]
        p3val=[]
        for i in p2:
            p2val.append(i.val)
        for i in p3:
            p3val.append(i.val)
        #print(p2val,p3val) 
        #print(p2,p3)
        for i in range(min(len(p2),len(p3))):
            if p2[i].val==p3[i].val:
                ans=p2[i]
        #print(ans)
        return ans
        