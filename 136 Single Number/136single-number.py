class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for i,v in enumerate(nums):
            res^=v
        return res
         