# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q=[]
        q.append(root)
        par1=[]
        par2=[]
        lvl=0
        while(q):
            f=len(q)
            while(f):
                r=q.pop(0)
                if r.left:
                    if r.left.val==x:
                        par1=[r.val,lvl]
                    if r.left.val==y:
                        par2=[r.val,lvl]
                    q.append(r.left)
                if r.right:
                    if r.right.val==x:
                        par1=[r.val,lvl]
                    if r.right.val==y:
                        par2=[r.val,lvl]
                    q.append(r.right)
                f-=1
            lvl+=1
        if par1==[] or par2==[]:
            return 0
        #print(par1,par2)
        if par1[1]==par2[1] and par1[0]!=par2[0]:
            return 1
        return 0
                    
                
        