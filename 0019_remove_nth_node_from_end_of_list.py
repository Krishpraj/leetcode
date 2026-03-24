# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        size = 0
        temp = head
        while temp:
            size += 1
            temp = temp.next

        n = size - n  # index from start (0-based)

        current = head
        prev = None

        if n == 0:
            return head.next  # delete head

        while n > 0:
            prev = current
            current = current.next
            n -= 1

        prev.next = current.next
        return head