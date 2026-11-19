class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        smaller=-1
        equal=0

        for i in range(len(nums)):
            if nums[i]<target:
                smaller+=1
            elif nums[i]==target:
                equal+=1

        res=[]
        for i in range(1,equal+1):
            res.append(smaller+i)

        return res
