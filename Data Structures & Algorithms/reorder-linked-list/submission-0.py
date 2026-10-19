# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        arr2=slow.next
        prev=None
        slow.next=None
        while arr2:
            temp=arr2.next
            arr2.next=prev
            prev=arr2
            arr2=temp
        first,sec=head,prev
        while sec:
            t1,t2=first.next,sec.next
            first.next=sec
            sec.next=t1
            first,sec=t1,t2