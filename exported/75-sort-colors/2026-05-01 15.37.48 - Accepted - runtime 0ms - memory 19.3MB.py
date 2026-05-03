class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        mp={}
        for i in range(len(nums)):
            if nums[i] in mp:
                mp[nums[i]]+=1
            else:
                mp[nums[i]]=1
        
        zeroes = mp.get(0, 0)
        ones = mp.get(1, 0)
        twos = mp.get(2, 0)

        nums[0:zeroes] = [0] * zeroes
        nums[zeroes:zeroes+ones] = [1] * ones
        nums[zeroes+ones:] = [2] * twos
                

