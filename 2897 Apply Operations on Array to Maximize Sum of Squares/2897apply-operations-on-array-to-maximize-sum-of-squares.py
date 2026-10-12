class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        
        b=[0]*30
        sm=0
        for i in nums:
            for j in range(30):
                if (i>>j)&1==1:
                    b[j]+=1
        
       
        for i in range(k):
            x=0
            for j in range(len(b)-1,-1,-1):
                x=x<<1
                if b[j]>0:
                    x=x|1
                    b[j]-=1
                
            print(x)
            sm+=x*x
        
        return sm%(10**9+7)
            
        