class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        
        prefix=[0]*len(nums)
        suffix=[0]*len(nums)

        for i in range(len(nums)): 
            if i>0: 
                prefix[i]+=prefix[i-1]
            prefix[i]+=nums[i]

        for j in range(len(nums)-1,-1,-1): 
            if j<len(nums)-1: 
                suffix[j]+=suffix[j+1]
            suffix[j]+=nums[j]
        

        for i in range(len(nums)):
            
            pre=0
            suf=0 

            if i>0:
                pre+=prefix[i-1]

            if i<len(nums)-1:
                suf+=suffix[i+1]

            if pre==suf:
                return i

        return -1
