class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        res=[]
        ans=[]
        def dfs(index):
            if ans not in res:
                res.append(ans[:])

            if index==len(nums):
                return 

            for i in range(index,len(nums)):
                ans.append(nums[i])
                dfs(i+1)
                ans.pop()
        dfs(0)
        return res
