class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count=0
        while n!=0: 
            x=n&1
            n=n>>1
            if x==1:
                count+=1
        
        return count