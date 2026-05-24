class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        rotten=[]
        oranges=0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    rotten.append((i,j))
        
        time=0
        while rotten:
            time+=1
            new_rotten=[]
            for r,c in rotten: 
                for dr,dc in directions:
                    if 0<=r+dr<len(grid) and 0<=c+dc<len(grid[0]) and grid[r+dr][c+dc]==1:
                        grid[r+dr][c+dc]=2
                        new_rotten.append((r+dr,c+dc))
            print(new_rotten,time)
            if len(new_rotten)==0: 
                time-=1
            rotten=new_rotten
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1 
        
        return time
        
        
        