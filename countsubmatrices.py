class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:

        count=0
        row={}
        for i in range(len(grid)):
            ans=[]
            for j in range(len(grid[0])):
                sm=grid[i][j]
                if j in row:
                    sm+=row[j]

                if sm+sum(ans)<=k:
                    count+=1

                if j in row:
                    row[j]+=grid[i][j]     
                else:
                    row[j]=grid[i][j]
                ans.append(sm)
        return count 
