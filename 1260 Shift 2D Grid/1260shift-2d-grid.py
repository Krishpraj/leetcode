class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        def shift(grid):
            curr=grid[-1][-1]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    temp=grid[i][j]
                    grid[i][j]=curr
                    curr=temp

        for i in range(k):
            shift(grid)
        return grid 

        