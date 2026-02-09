
from ast import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        se=set()
        ans=[]
        def dfs():
            if len(ans)==len(nums):
                se.add(tuple(ans[:]))

            for i in range(len(nums)):
                if nums[i] not in ans:
                    ans.append(nums[i])
                    dfs()
                    ans.pop()
        
        dfs()
        return list(se)
