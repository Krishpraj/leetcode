class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        
        for i in range(len(nums)):
            curr=abs(nums[i])
            if nums[curr]<0:
                return curr
            nums[curr]=-nums[curr]

