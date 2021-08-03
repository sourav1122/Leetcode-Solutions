# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        def call(root,valu):
            nonlocal count
            if root==None:
                return 
            
            if root.val>=valu:
                count+=1
                #print(root.val,valu,count)
            call(root.left,max(root.val,valu))
            call(root.right,max(root.val,valu))
        call(root,root.val)
        return count
                
                
            
        