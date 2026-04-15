class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:

        # [1,2,3]
        
        i=start
        rev_i=start
        while True:
            if nums[i]==target:
                return abs(i-start) 
            elif nums[rev_i]==target:
                return abs(rev_i-start)
            
            if i<len(nums)-1:
                i+=1

            if rev_i>0:
                rev_i-=1
            

            
