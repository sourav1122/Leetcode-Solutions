# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp={}
        def robbe(roote):
            if roote==None:
                return 0
            if roote in dp:
                return dp[roote]
            incl=roote.val
            if roote.left!=None:
                incl+=robbe(roote.left.left)+robbe(roote.left.right)
            if roote.right!=None:
                incl+=robbe(roote.right.left)+robbe(roote.right.right)
            excl=robbe(roote.left)+robbe(roote.right)
            dp[roote]= max(incl,excl)
            return dp[roote]
        return robbe(root)
        