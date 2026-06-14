# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        length=0
        arr=[]
        curr=head
        while curr: 
            
            arr.append(curr.val)
            curr=curr.next
            length+=1

        mx=float('-inf')
        for i in range(length):
            mx=max(mx,arr[i]+arr[length-1-i])
        
        return mx
        