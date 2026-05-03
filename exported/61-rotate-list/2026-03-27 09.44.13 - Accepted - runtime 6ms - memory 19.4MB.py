# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        if not head:
            return head 

        def rotate(node):
            last=node
            while last.next:
                last=last.next
            last=last.val

            prev=last
            curr=node
            while curr:
                temp=curr.val
                curr.val=prev
                prev=temp
                curr=curr.next


        curr=head
        length=0
        while curr:
            curr=curr.next
            length+=1


        rotations=0
        k=k%length
        while rotations<k:
            rotate(head)
            rotations+=1

        return head