# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def heigh(roote):
            if roote==None:
                return 0
            lh=heigh(roote.left)
            if lh==-1:
                return -1
            rh=heigh(roote.right)
            if rh==-1:
                return -1
            if abs(lh-rh)>1:
                return -1
            return max(lh,rh)+1
        #print(heigh(root))
        if heigh(root)==-1:
            return 0
        return 1