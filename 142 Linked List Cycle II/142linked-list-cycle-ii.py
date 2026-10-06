# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mp={}
        pos=0
        curr=head

        while curr:
            if curr in mp:
                return curr
            else:
                mp[curr]=pos
                pos+=1
                curr=curr.next

        return None