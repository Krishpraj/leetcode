class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:


        dp=0
        sm=sum(nums)
        for i in range(len(nums)):
            dp+=nums[i]*i
        ans=dp

        for i in range(1,len(nums)):
            dp=dp+sm-len(nums)*nums[-i]
            ans=max(ans,dp)
        return ans