class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        mp={}

        for i in range(len(nums)):
            mp[(i+k)%len(nums)]=nums[i]
        
        print(mp)
    
        for i,v in mp.items():
            nums[i]=v
        
        return nums