# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev=None
        curr=head
        nxt=curr.next
        idx=0


        ctc=[]
        while nxt:
            if prev and nxt:
                if curr.val<prev.val and curr.val<nxt.val:
                    ctc.append(idx)
                if curr.val>prev.val and curr.val>nxt.val:
                    ctc.append(idx)
            idx+=1
            prev=curr
            curr=curr.next
            nxt=curr.next

        if len(ctc)<2:
            return [-1,-1]

        else:
            ctc.sort()
            print(ctc)
            mn=float("inf")
            for i in range(1,len(ctc)):
                mn=min(mn,ctc[i]-ctc[i-1])
            return [mn, ctc[-1]-ctc[0]]




        