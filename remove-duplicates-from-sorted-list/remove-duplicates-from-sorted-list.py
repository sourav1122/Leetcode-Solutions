# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head==None:
            return head
        temp1=head
        temp2=head.next
        #s=set()
        if temp2==None:
            return head
        while(temp2):
            if temp1.val==temp2.val:
                #s.add(temp1.val)
                temp2=temp2.next
                temp1.next=temp2
                
            else:
                temp2=temp2.next
                temp1=temp1.next
        return head