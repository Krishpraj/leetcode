class Solution:
    def dominantIndices(self, nums: List[int]) -> int:

        count=0
        for i in range(len(nums)-1):
            print(sum(nums[i+1:len(nums)])/(len(nums)-i+1))
            if nums[i]>((sum(nums[i+1:len(nums)]))/(len(nums)-i-1)):
                count+=1
        return count
        