class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates=sorted(candidates)

        res=[]
        ans=[]

        visited=set()

        def dfs(start):
            if sum(ans)>target:
                return 
            elif sum(ans)==target:
                res.append(ans[:])
                return 

            for i in range(start,len(candidates)):
                    if i>start and candidates[i]==candidates[i-1]:
                        continue
                    ans.append(candidates[i])
                    dfs(i+1)
                    ans.pop()
            
        dfs(0)
        print(res)
        if not res:
            return []
        else:
            return list(res)
        