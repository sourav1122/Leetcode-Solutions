# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        inorder=[]
        if root==None:
            return None
        ans=[]
        def inorder(root):
            #print(ans)
            if root==None:
                return 
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        inorder(root)
        #print(ans)
        if sorted(ans)==ans and len(set(ans))==len(ans):
            return 1
        return 0
                    
                    
        