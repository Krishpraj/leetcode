class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        

        res={}
        for i in range(len(nums)-1,-1,-1):
            longest=0
            for j,v in res.items(): 
                if j>nums[i]:
                    longest=max(longest,res[j])
            res[nums[i]]=longest+1
        
        return max(res.values())
