# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       
        l3=ListNode(0)
        head=l3 
        carry=0
        while l1 and l2: 
            temp=l1.val+l2.val+carry 
            l3.val=temp%10
            carry=temp//10
            l1=l1.next 
            l2=l2.next 
            newnode=ListNode(0)
            if l1 and l2:
                l3.next=newnode
                l3=l3.next
        while l1:
            temp=l1.val+carry
            newnode=ListNode(temp%10)
            carry=temp//10
            l3.next=newnode
            l3=l3.next
            l1=l1.next
        while l2:
            temp=l2.val+carry
            newnode=ListNode(temp%10)
            carry=temp//10
            l3.next=newnode
            l3=l3.next
            l2=l2.next
        if carry:
            newnode=ListNode(carry)
            l3.next=newnode
        return head


        


            