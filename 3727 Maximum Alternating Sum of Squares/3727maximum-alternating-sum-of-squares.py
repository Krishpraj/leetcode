class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums=[abs(i) for i in nums]
        nums.sort(reverse=True)
        l=0
        r=len(nums)-1

        
        score=0
        if len(nums)%2==1:
            score+=nums[l]**2
            l+=1
        while l<r:
            score+=nums[l]**2
            score-=nums[r]**2
            l+=1
            r-=1
        
        return score
        