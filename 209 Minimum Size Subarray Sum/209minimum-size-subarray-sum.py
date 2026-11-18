class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        

        curr_sum=0
        min_length=float('inf')

        l=0
        
        for r in range(len(nums)):
            curr_sum+=nums[r]
            while curr_sum>=target:
                min_length=min(min_length,r-l+1)
                curr_sum-=nums[l]
                l+=1
        
        if min_length==float('inf'):
            return 0
        return min_length
