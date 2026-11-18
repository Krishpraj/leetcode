class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        arr=zip(startTime,endTime,profit)
        arr=sorted(arr)

        startTime=[c[0] for c in arr]
        endTime=[c[1] for c in arr]
        profit=[c[2] for c in arr]


        
        dp=[0]*(max(startTime)+2) #[3,4,5,6]  #[0,0,0,0,0,0,0]
        curr=len(startTime)-1
        
        for i in range(len(dp)-2,0,-1):
            dp[i]=dp[i+1]
            while curr>=0 and i==startTime[curr]:
                mx=profit[curr]
                if endTime[curr]<len(dp):
                    mx+=dp[endTime[curr]] 
                dp[i]=max(mx,dp[i])
                curr-=1
        
        return dp[1]