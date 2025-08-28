class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res=[]
        ans=[]

        used = [False] * len(nums)
        def backtrack():


            if ans not in res and len(ans)==len(nums):
                res.append(ans[:])
            

            for i in range(len(nums)):
                if not used[i]:
                    used[i]=True
                    ans.append(nums[i])
                    backtrack()
                    ans.pop()
                    used[i]=False


        backtrack()
        return res