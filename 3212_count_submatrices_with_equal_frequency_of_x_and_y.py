class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        count=0
        row={}
        xrow={}
        for i in range(len(grid)):
            prefix=0
            xprefix=0
            for j in range(len(grid[0])):
                if j in row:
                    prefix+=row[j]
                if j in xrow:
                    xprefix+=xrow[j]
                if grid[i][j]=="X":
                    prefix+=1
                    xprefix+=1
                    if j in row:
                        row[j]+=1
                    else:
                        row[j]=1
                    if j in xrow:
                        xrow[j]+=1
                    else:
                        xrow[j]=1
                elif grid[i][j]=="Y":
                    prefix-=1
                    if j in row:
                        row[j]-=1
                    else:
                        row[j]=-1

                if prefix==0 and xprefix>0:
                    count+=1
            
        return count
