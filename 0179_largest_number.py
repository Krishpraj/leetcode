class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums= [str(i) for i in nums]
        nums.sort(key=lambda x:x*10 , reverse=True)
        
        if sum([int(i) for i in nums])==0:
            return "0"

        return "".join(nums)
