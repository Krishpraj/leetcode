class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        breakpoint=None

        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                breakpoint = i
                break
        
        print(breakpoint)
        
        if breakpoint==None:
            nums.reverse()
        else:
            smallest=None 
            for i in range(len(nums)-1,breakpoint,-1):
                if nums[breakpoint]<nums[i]:
                    if smallest is None or nums[i] < nums[smallest]:
                        smallest = i
            
            nums[breakpoint],nums[smallest]=nums[smallest],nums[breakpoint]
            print(nums)
            nums[breakpoint+1:] = nums[breakpoint+1:][::-1]
            print(nums)
            

        
            