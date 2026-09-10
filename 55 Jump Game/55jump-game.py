class Solution:
    def canJump(self, nums: List[int]) -> bool:

        mx=0
        for i in range(len(nums)):
            if i+nums[i]>mx and i<=mx:
                mx=i+nums[i]


        return mx>=len(nums)-1                    