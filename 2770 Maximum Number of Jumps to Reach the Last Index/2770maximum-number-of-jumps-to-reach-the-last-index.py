class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:

        
        dp={}

        def dfs(i,j):
            if i in dp:
                return dp[i]

            if i==len(nums)-1:
                return 0 
            
            elif j>=len(nums):
                return float("-inf")
            
            else:
                skip=float("-inf")
                if abs(nums[j]-nums[i])<=target:
                    skip=dfs(j,j+1)+1
                no_skip=dfs(i,j+1)
                
                dp[i]=max(skip,no_skip)
                return max(skip,no_skip) 

        ans=dfs(0,1)
       
        if ans!=float("-inf"):
            return ans
        else:
            return -1 