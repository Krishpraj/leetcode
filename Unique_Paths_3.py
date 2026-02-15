class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        empty=0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] >= 0:
                    empty += 1
                if grid[r][c] == 1:
                    start_r, start_c = r, c

        def dfs(r,c,remain):
            
            if r>=rows or c>=cols or r < 0 or c < 0 or grid[r][c]==-1:
                return 0
            elif grid[r][c]==2:
                return 1 if remain==1 else 0 
            else:
                paths=0
                temp=grid[r][c]
                grid[r][c]=-1
                for dr,dc in directions:
                    paths+=dfs(r+dr,c+dc,remain-1)
                grid[r][c]=temp
                return paths

        return dfs(start_r,start_c,empty)
       
