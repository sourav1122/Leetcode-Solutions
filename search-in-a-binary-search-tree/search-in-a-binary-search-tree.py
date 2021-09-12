# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def searche(roote):
            if roote==None:
                return 
            if roote.val==val:
                return roote
            if val>roote.val:
                return searche(roote.right)
            else:
                return searche(roote.left)
        return searche(root)
            