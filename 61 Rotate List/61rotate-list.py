# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        nodes=[]
        size=0
        curr=head

        if not curr:
            return None

        while curr:
            nodes.append(curr)
            curr=curr.next
            size+=1

        mp={}

        print(nodes,size,k)
        for i,v in enumerate(nodes):
            mp[(i+k)%size]=v
     
        for i in range(size):
            if i==size-1:
                mp[i].next=None
            else:
                mp[i].next=mp[i+1]

        return mp[0] 
    
        