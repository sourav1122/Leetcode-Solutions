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
        head = root
        while head and head.left:
            x = head
            while x:
                x.left.next = x.right
                if x.next:
                    x.right.next = x.next.left
                x = x.next
            #print(head)
            head = head.left
        return root
            
        
            
            
                    