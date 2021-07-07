# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        def solve(ra,rb):
            if rb==None :
                return ra
            if ra==None :
                return rb
            ra.val+=rb.val
            ra.left=solve(ra.left,rb.left)
            ra.right=solve(ra.right,rb.right)
            return ra
              
        return   solve(root1,root2)
         
                
            
        