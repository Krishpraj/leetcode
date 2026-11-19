class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

       

        prefix=[1]*len(nums)
        suffix=[1]*len(nums)
        for i in range(len(nums)):
            prefix[i]*=nums[i]
            if i>0: 
                prefix[i]*=prefix[i-1]

        for j in range(len(nums)-1,-1,-1):
            suffix[j]*=nums[j]
            if j<len(nums)-1:
                suffix[j]*=suffix[j+1]


        for i in range(len(nums)):
            nums[i]=1
            if i>0: 
                nums[i]*=prefix[i-1]
            if i<len(nums)-1:
                nums[i]*=suffix[i+1]

        return nums          