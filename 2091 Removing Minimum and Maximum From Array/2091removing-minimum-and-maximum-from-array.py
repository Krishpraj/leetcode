class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        id1=nums.index(max(nums))
        id2=nums.index(min(nums))
        
        return min(id1+1+len(nums)-id2,id2+1+len(nums)-id1,max(id1,id2)+1, max(len(nums)-id1,len(nums)-id2))
        


            