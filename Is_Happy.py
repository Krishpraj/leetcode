class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen=set()
        while n not in seen: 
            seen.add(n)
            stk=[int(c) for c in str(n)]
            total=0
            for i in stk:
                total+=i**2
            n=total
            if n==1:
                return True 
        
        return False 
