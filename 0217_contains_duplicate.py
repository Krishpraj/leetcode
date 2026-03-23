from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        se=set()
        for i in range(len(nums)):
            if nums[i] in se:
                return True 
            se.add(nums[i])
        
        return False 
        

