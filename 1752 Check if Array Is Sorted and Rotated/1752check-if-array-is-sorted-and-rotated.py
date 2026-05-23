class Solution:
    def check(self, nums: List[int]) -> bool:
        for j in range(len(nums)):
            i=j
            prev=float("-inf")
            while i<j+len(nums):
                if nums[i%len(nums)]>=prev:
                    prev=nums[i%len(nums)]
                    i+=1
                    continue
                else:
                    break
            if i==j+len(nums):
                return True 

        return False 
