# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxid=0
        def diffe(roote):
            nonlocal maxid
            if roote==None:
                return [999999999,-999999999]
            if roote.left==None and roote.right==None:
                return [roote.val,roote.val]
            lefte=diffe(roote.left)
            righte=diffe(roote.right)
            
            if lefte==[999999999,-999999999]:
                #print(maxid,"before")
                maxid=max(maxid,abs(roote.val-righte[0]),abs(roote.val-righte[1]))
                to_return =[min(roote.val,righte[0]),max(roote.val,righte[1])]
                #print(righte,maxid,"after")
            elif righte==[999999999,-999999999]:
                maxid=max(maxid,abs(roote.val-lefte[0]),abs(roote.val-lefte[1]))
                to_return =[min(roote.val,lefte[0]),max(roote.val,lefte[1])]
            else:
                maxid=max(maxid,abs(roote.val-lefte[0]),abs(roote.val- lefte[1]),abs(roote.val-righte[0]),abs(roote.val-righte[1]))
                to_return =[min(roote.val,lefte[0],righte[0]),max(roote.val,lefte[1],righte[1])]
            #print(lefte,righte,roote.val,maxid)
            #print(to_return)
            return to_return 
        
        diffe(root)
        return maxid