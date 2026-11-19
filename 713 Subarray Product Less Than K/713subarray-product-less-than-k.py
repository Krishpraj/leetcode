class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        
        # [10,5,2,6]
        # 10 
        # 50 counted
        # 100 counted 
        # 600 nout counted 

        if k<=1: 
            return 0 
        
        count=0
        l=0 
        curr=1
        for r in range(len(nums)):
            curr*=nums[r]
            while curr>=k: 
                curr=curr//nums[l]
                l+=1 
            count+=1+(r-l)
        
        return count

