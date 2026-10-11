class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:

       sm=0

       for i,v in enumerate(nums):
        if len(nums)%(i+1)==0:
            sm+=v**2

       return sm 