class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # rotations is k%3
        # head is going to change

        if not head:
            return None 

        stk=[]
        count=0
        temp=head
        while temp:
            stk.append(temp)
            count+=1
            temp=temp.next
        
        k=k%count
        while k>0:
            node=stk.pop()
            node.next=head
            head=node
            k-=1
        
        last=stk.pop()
        last.next=None 

        return head
        
