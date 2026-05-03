class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res=[]
        ans=[]

        def dfs(opened,closed):
            print(ans)
            if opened==closed==n:
                res.append("".join(ans))
                return

            if opened<n:
                ans.append("(")
                dfs(opened+1,closed)
                ans.pop()
            
            if opened>closed:
                ans.append(")")
                dfs(opened,closed+1)
                ans.pop()
        
        dfs(0,0)
        return res