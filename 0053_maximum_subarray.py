class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mxsum=0
        mx=float('-inf')
        l=0
        r=l
        while r<len(nums):
            while mxsum<0:
                mxsum-=nums[l]
                l+=1
            mxsum+=nums[r]
            r+=1
            mx=max(mxsum,mx)
        return mx



        
