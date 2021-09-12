# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def semit(rootea,rooteb):
            if rootea==None and rooteb==None:
                return 1
            
            if (rootea==None or rooteb==None):
                #print("YAHA")
                return 0
            #print(rootea.val,rooteb.val)
            if rootea.val!=rooteb.val:
                return 0
            return semit(rootea.left,rooteb.right) and semit(rootea.right,rooteb.left)
        return semit(root.left,root.right)