# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi=root.val
        def dfs(roote):
            nonlocal maxi
            if roote==None:
                return 0
            lval=max(0,dfs(roote.left))
            rval=max(0,dfs(roote.right))
            maxi=max(maxi,roote.val+lval+rval)
            #print(maxi)
            return roote.val+max(lval,rval)
        dfs(root)
        return  maxi
            