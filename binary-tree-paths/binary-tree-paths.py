# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        l=[]
        def dfs(roote,ans):
            nonlocal l
            if roote==None:
                return 
            if roote.left==None and roote.right==None:
                ans.append(roote.val)
                l.append(ans)
                return 
            dfs(roote.left,ans+[roote.val])
            dfs(roote.right,ans+[roote.val])
        dfs(root,[])
        fans=[]
        for i in l:
            x=i
            st=""
            #print(x)
            for j in range(len(x)-1):
                st+=str(x[j])
                st+="->"
            st+=str(x[len(x)-1])
            fans.append(st)
        return fans