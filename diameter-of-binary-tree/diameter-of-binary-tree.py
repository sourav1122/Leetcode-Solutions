# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi=0
        def dfs(roote):
            nonlocal maxi
            if roote==None:
                return 0
            l=dfs(roote.left)
            r=dfs(roote.right)
            maxi=max(l+r,maxi)
            return 1+max(l,r)
        dfs(root)
        return maxi