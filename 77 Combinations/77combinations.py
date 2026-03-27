class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        

        res=[]
        ans=[]
        def dfs(idx):
            if len(ans)==k:
                res.append(ans[:])
                return 

            for i in range(idx,n+1):
                ans.append(i)
                dfs(i+1)
                ans.pop()

        dfs(1)
        return res 