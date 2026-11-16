class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        nums=set(nums)
        mx=0
        for num in nums:
            if num-1 in nums:
                continue 
            else:
                length=1
                while num+1 in nums:
                    length+=1
                    num+=1
                mx=max(length,mx)
        
        return mx 









                