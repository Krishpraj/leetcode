class Solution:
    def numTrees(self, n: int) -> int:
        
        dp=[]
        for i in range(n+1):
            if i==1 or i==0:
                dp.append(1)
            else:
                curr=0
                for j in range(i):
                    print(j,i-j)
                    curr+=dp[j]*dp[i-j-1]
                dp.append(curr)
            print(dp)
        return dp[-1]
