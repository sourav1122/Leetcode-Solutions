# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def calc(roote):
            global sumi
            if roote==None:
                return 
            if low<=roote.val<=high:
                sumi+=roote.val
            calc(roote.left)
            calc(roote.right)
        global sumi
        sumi=0
        calc(root)
        return sumi
            
        