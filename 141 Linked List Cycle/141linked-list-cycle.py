# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        curr=head
        se=set()
        
        while curr:
            if curr in se:
                return True 
            se.add(curr)
            curr=curr.next
        
        return False 

