class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l=0
        r=len(numbers)-1
        nums=numbers

        while l<r:
            if nums[l]+nums[r]>target:
                r-=1
            elif nums[l]+nums[r]<target:
                l+=1
            else:
                return [l+1,r+1]

        