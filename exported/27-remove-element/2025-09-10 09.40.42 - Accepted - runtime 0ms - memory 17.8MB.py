class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r=0

        while r<len(nums):
            if nums[r]==val:
                nums.pop(r)
            else:
                r+=1
        return len(nums)