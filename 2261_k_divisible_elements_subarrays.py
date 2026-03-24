class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        
      

        def isdivisible(arr):
            count=0
            for i in arr:
                if i%p==0:
                    count+=1

            if count>k:
                return False 
            return True 

        count=set()

        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                if isdivisible(nums[i:j]):
                    count.add(tuple(nums[i:j]))

        return len(count)
               
            
        
            
            
