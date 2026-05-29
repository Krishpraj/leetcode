class Solution:
    def minElement(self, nums: List[int]) -> int:
        
        res=[]
        for i in range(len(nums)): 
            x=str(nums[i])
            res.append(sum([int(c) for c in x]))
        
        return min(res)