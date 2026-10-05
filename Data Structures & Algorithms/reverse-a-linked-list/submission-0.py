# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        curr=head
        while curr!= None:
            arr.append(curr.val)
            curr=curr.next
        arr.reverse()
        dummy=ListNode(0)
        current=dummy
        for i in arr:
            current.next=ListNode(i)
            current=current.next
        dummy=dummy.next
        return dummy
