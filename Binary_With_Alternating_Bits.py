class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        prev=0
        while n!=0:
            prev=n&1
            n=n>>1
            if (n&1)==prev:
                return False
            
        return True 
