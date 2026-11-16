class Solution:
    def climbStairs(self, n: int) -> int:
       
       #step 1  1
       # step 2  2 step1+1 or step0+2 
       # step 3 step2+1 step1+2


       dp={}

       for i in range(1,n+1):
            if i==1:
                dp[i]=1
            elif i==2:
                dp[i]=2 
            else:
                dp[i]=dp[i-1]+dp[i-2]

       return dp[n]