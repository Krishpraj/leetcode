class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
    
        res=set()
        ans=[]
        def dfs():
            if sum(ans)>target:
                return 
            elif sum(ans)==target:
                res.add(tuple(sorted(ans[:])))

            for i in range(len(candidates)):
                ans.append(candidates[i])
                dfs()
                ans.pop()
        
        dfs()
        return list(res)
        