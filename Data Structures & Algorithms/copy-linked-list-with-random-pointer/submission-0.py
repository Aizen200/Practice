"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        obj={None:None}
        curr=head
        while curr:
            x=Node(curr.val)
            obj[curr]=x
            curr=curr.next
        ans=head
        while ans:
            val=obj[ans]
            val.next=obj[ans.next]
            val.random=obj[ans.random]
            ans=ans.next
        return obj[head]
