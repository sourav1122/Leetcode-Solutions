# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inver(root):
            if root==None:
                return None
            l=inver(root.left)
            r=inver(root.right)
            root.left=r
            root.right=l
            return root
        inver(root)
        return root