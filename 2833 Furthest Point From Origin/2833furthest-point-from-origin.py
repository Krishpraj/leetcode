class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        
        moves=[c for c in moves]
        mx=0
        curr=0
        for i in moves:
            if i=='R':
                curr+=1
            if i=='L':
                curr-=1
            if i=='_':
                curr-=1
        mx=max(mx,abs(curr))
       

        curr=0
        for i in moves:
            if i=='R':
                curr+=1
            if i=='L':
                curr-=1
            if i=='_':
                curr+=1
        mx=max(mx,abs(curr))

        return mx

