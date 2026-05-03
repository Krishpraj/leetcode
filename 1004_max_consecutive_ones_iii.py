class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        l=0
        r=0
        ans=0
        flips=0
        

        while r<len(nums):
            if nums[r]==1:
                ans=max(ans,r-l+1)
            elif nums[r]==0:
                if flips<k:
                    ans=max(ans,r-l+1)
                    flips+=1
                else:
                    while nums[l]!=0:
                        l+=1
                    l+=1
                    ans=max(ans,r-l+1)

            r+=1
        
        return ans 
                