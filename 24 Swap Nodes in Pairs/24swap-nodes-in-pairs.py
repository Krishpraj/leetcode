# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
       curr=head
       nodes=[]
       while curr:
        nodes.append(curr)
        curr=curr.next
       if len(nodes)<=1:
        return head

       for i in range(0,len(nodes),2):
        if i+1<len(nodes):
            nodes[i],nodes[i+1]=nodes[i+1],nodes[i]
            
     
       for i in range(len(nodes)):
        if i==len(nodes)-1:
            nodes[i].next=None 
        else:
            nodes[i].next=nodes[i+1]
       return nodes[0]