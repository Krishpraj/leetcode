class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        edge=min(len(grid), len(grid[0])) // 2 -1
       
        row=len(grid[0])
        height=len(grid)

        while edge>=0:
            res=[]
            for i in range(edge,len(grid[0])-edge):
                res.append(grid[edge][i])
            
            for i in range(edge+1,len(grid)-edge-1):
                res.append(grid[i][row-edge-1])

            for i in range(len(grid[0])-edge-1,edge-1,-1):
                res.append(grid[height-edge-1][i])

            for i in range(len(grid)-edge-2,edge,-1):
                res.append(grid[i][edge])

          
            x=k%len(res)
            size=len(res)
            res=res*2
            res=res[x:size+x][::-1]

            print(res)

            for i in range(edge,len(grid[0])-edge):
                grid[edge][i]=res[-1]
                res.pop()

            for i in range(edge+1,len(grid)-edge-1):
                grid[i][row-edge-1]=res[-1]
                res.pop()

            for i in range(len(grid[0])-edge-1,edge-1,-1):
                grid[height-edge-1][i]=res[-1]
                res.pop()

            for i in range(len(grid)-edge-2,edge,-1):
                grid[i][edge]=res[-1]
                res.pop()
            
            edge-=1
            
          


        
        return grid
        
        