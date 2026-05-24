class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp={}
        dp[0]=1
     
        for i in range(1,amount+1):
            minimum_coins=float("inf")
            for j in coins: 
            
                if i-j in dp:
                    minimum_coins=min(dp[i-j]+1,minimum_coins)
                
            dp[i]=minimum_coins
       
        if dp[amount]-1==float("inf"):
            return -1 
        return dp[amount]-1

         



        # do all paths if we find a paht with less change dp[how many coins]