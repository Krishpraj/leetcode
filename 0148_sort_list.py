class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        stk=[]
        while head:
            stk.append(head)
            head=head.next

        stk.sort(key=lambda x:x.val)
        
        for i in range(len(stk)):
            if i==len(stk)-1:
                stk[i].next=None
            else:
                stk[i].next=stk[i+1]
        
        if stk:
            return stk[0]
        else:
            return None
