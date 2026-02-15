class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows,cols=len(obstacleGrid),len(obstacleGrid[0])

        if obstacleGrid[rows-1][cols-1]==1:
            return 0 

        memo={}
        def dfs(r,c):
            if r==rows-1 and c==cols-1:
                return 1 
            elif r>=rows or c>=cols or obstacleGrid[r][c]==1:
                return 0
            elif (r,c) in memo:
                return memo[(r,c)]
            else:
                memo[(r,c)]=dfs(r+1,c)+dfs(r,c+1)
                return memo[(r,c)]
        return dfs(0,0)
       
    