# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def maketr(roote,ele):
            if roote is None:
                return TreeNode(ele)
            if roote.val>ele:
                roote.left=maketr(roote.left,ele)
            else:
                roote.right=maketr(roote.right,ele)
            return roote
        roote=None
        for i in preorder:
            roote=maketr(roote,i)
            print(roote)
        return roote