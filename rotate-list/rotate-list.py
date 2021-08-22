# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:
            return head
        temp1=head
        l=0
        while(temp1.next!=None):
            temp1=temp1.next
            l+=1
        l+=1
        temp1.next=head
        k=k%l
        f=l-k-1
        temp2=head
        while(f!=0):
            temp2=temp2.next
            f-=1
        #print(temp2)
        #print(temp1)
        head=temp2.next
        temp2.next=None
        
        return head
            
            
        
        