class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        
        memo={}

        def dfs(i,j,o,c):

            if not 0<=i<len(grid) or not 0<=j<len(grid[0]):
                return False  


            if grid[i][j]=="(":
                o+=1
            else:
                c+=1
            
            if (i,j,o,c) in memo:
                return memo[(i,j,o,c)]

            
            if c>o:
                return False 

            if i==len(grid)-1 and j==len(grid[0])-1 and o==c:
                return True 

            else:
                ans= dfs(i+1,j,o,c) or dfs(i,j+1,o,c)
                memo[(i,j,o,c)]=ans
                return ans 

        return dfs(0,0,0,0)
