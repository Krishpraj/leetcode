class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        i=1
        mx=1
        ans=0
        while i<len(nums):
            if nums[i]>nums[i-1]:
                mx+=1
            else:
                mx=1
            ans=max(mx,ans)
            i+=1
        return max(ans,1)