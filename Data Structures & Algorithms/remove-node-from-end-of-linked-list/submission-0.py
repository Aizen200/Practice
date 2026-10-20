# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev=None
        while head:
            tmp=head.next
            head.next=prev
            prev=head
            head=tmp
        curr=prev
        if n==1:
            prev=prev.next
        else:
            count=1
            while count<n-1:
                count+=1
                curr=curr.next
            curr.next=curr.next.next
        fin=None
        while prev:
            tmp2=prev.next
            prev.next=fin
            fin=prev
            prev=tmp2
        return fin

        