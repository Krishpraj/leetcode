class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=0
        r=0
        ans=0
        curr=0
        
        while r<len(nums):
            if nums[r]==1:
                curr+=1
            else:
                curr=0
            
            ans=max(ans,curr)
            r+=1
        return ans 
        