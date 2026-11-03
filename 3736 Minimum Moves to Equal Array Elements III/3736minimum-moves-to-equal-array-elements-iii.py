class Solution:
    def minMoves(self, nums: List[int]) -> int:

        sm=0
        mx=max(nums)
        for i in range(len(nums)):
           sm+=mx-nums[i]
        
        return sm 


        
        