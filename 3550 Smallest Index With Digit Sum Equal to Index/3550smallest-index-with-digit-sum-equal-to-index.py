class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        for i,v in enumerate(nums):
            if sum([int(j) for j in str(v)])==i:
                return i 
        
        return -1 