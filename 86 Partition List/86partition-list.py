# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        if not head:
            return head

        nodes=[]
        
        curr=head

        while curr:
            nodes.append(curr)
            curr=curr.next
        
        i=0

        # nodes less than value x come before nodes greater or equal to x 

        for i in range(len(nodes)):
            if nodes[i].val<x:
                print([i.val for i in nodes])
                idx=i-1
                curr=i
                while idx>=0 and nodes[idx].val>=x:
                    nodes[idx],nodes[curr]=nodes[curr],nodes[idx]
                    idx-=1
                    curr-=1
        
        head=nodes[0]
        for i in range(len(nodes)):
            if i==len(nodes)-1:
                nodes[i].next=None
            else:
                nodes[i].next=nodes[i+1]
        return head
        
                
                   