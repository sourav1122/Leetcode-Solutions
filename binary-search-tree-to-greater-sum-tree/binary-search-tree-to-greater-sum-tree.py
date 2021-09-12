# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        maxi=0
        def dfs(roote):
            nonlocal maxi
            if roote==None:
                return 0
            dfs(roote.right)
            maxi+=roote.val
            roote.val=maxi
            dfs(roote.left)
        dfs(root)
        return root