class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        ans=[]

        def dfs(opened,closed):
            nonlocal ans 
            if opened==closed and opened==n:
                res.append("".join(ans))
                return 

            if opened>=closed and opened<n:
                ans.append("(")
                dfs(opened+1,closed)
                ans.pop()
            
            if opened>closed:
                ans.append(")")
                dfs(opened,closed+1)
                ans.pop()
            
        dfs(0,0)
        return res
            
            
