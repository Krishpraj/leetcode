class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        res=set(nums)
        ans=[]
        for i in range(1,len(nums)+1):
            if i not in res:
                ans.append(i)
        return ans


        