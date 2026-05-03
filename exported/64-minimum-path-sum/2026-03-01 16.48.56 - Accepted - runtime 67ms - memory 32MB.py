class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        rows,cols=len(grid),len(grid[0])
        
        visited = {}
        def dfs(r,c):
        
            # base cases
            if r==rows-1 and c==cols-1:
                return grid[r][c]

            if (r, c) in visited:
                return visited[(r,c)]
            minsum = float('inf')

            for x,y in [(1,0), (0,1)]:
                if 0 <= x + r < rows and 0 <= y + c < cols:
                    minsum = min(grid[r][c] + dfs(x + r, y + c), minsum)

            visited[(r,c)] = minsum 
            return minsum
        
        return dfs(0, 0)
