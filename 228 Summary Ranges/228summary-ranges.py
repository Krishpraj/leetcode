class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        res=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]+1:
                if i+1<len(nums) and nums[i+1]==nums[i]+1:
                    continue
                else:
                    res[-1]+=f"->{nums[i]}"
            else:
                res.append(f"{nums[i]}")
        
        return res
