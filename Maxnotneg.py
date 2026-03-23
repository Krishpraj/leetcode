class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:

        prod={}
        prod[(0, 0)] = (grid[0][0], grid[0][0])
    
        def dfs(m,n):

            if m>=len(grid) or n>=len(grid[0]):
                return 
            
            current=grid[m][n]
            candidates=[]
            if (m-1,n) in prod:
                candidates.append(prod[(m-1,n)])
            if (m,n-1) in prod:
                candidates.append(prod[(m,n-1)])
            
            mini,maxi=float('inf'), float('-inf')
            for i in candidates:
                mini=min(current*i[0], current*i[1], mini)
                maxi=max(current*i[0], current*i[1], maxi)

            prod[(m,n)]=(mini,maxi)

        
        for i in range(len(grid)):
            for j in range(len(grid[0])): 
                if not (i == 0 and j == 0):
                    dfs(i, j)

        if prod[(len(grid)-1,len(grid[0])-1)][1]>=0:
            return prod[(len(grid)-1,len(grid[0])-1)][1]%(10**9 + 7)
        else:
            return -1

            
