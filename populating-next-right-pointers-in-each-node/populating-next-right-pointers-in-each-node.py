"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q=[]
        if root==None:
            return 
        q.append(root)
        
        while(q):
            f=len(q)
            for i in range(f-1):
                g1=q[i]
                g2=q[i+1]
                g1.next=g2
            q[f-1].next=None
            p=len(q)
            while(p):
                r=q.pop(0)
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
                p-=1
        return root
        
            
            
                    