class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:



        rows={}
        columns={}
        total=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i in rows:
                    rows[i]+=grid[i][j]
                else:   
                    rows[i]=grid[i][j]

                if j in columns:
                    columns[j]+=grid[i][j]
                else:
                    columns[j]=grid[i][j]
                total+=grid[i][j]
                
        rows=list(rows.values())
        cols=list(columns.values())

        sm=0
        for i in range(len(rows)):
            sm+=rows[i]
            if sm==total-sm:   
                return True
        sm=0
        for i in range(len(cols)):
            sm+=cols[i]
            if sm==total-sm:
                return True
        return False
               
        
