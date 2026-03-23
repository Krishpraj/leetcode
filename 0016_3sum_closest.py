
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums=sorted(nums)
        closest=float('inf')
        
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                sm=nums[i]+nums[l]+nums[r]
                if abs(sm-target)<abs(closest-target):
                    closest=sm
                if sm>target:
                    r-=1
                elif sm<target:
                    l+=1
                else:
                    l+=1
                    r-=1
                
        return closest 
    
