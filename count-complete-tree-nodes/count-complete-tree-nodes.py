# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def heightel(roote1):
            hght1=0
            while(roote1):
                hght1+=1
                roote1=roote1.left
            return hght1
        def heighter(roote2):
            hght2=0
            while(roote2):
                hght2+=1
                roote2=roote2.right
            return hght2
        def dfs(roote):
            if roote==None:
                return 0
            lh=heightel(roote)
            rh=heighter(roote)
            print(lh,rh,roote.val)
            if lh==rh:
                return (2**lh)-1
            
            return 1+dfs(roote.left)+dfs(roote.right)
        return dfs(root)

        