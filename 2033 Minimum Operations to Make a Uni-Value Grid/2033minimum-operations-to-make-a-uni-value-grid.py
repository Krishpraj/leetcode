class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        

        
        se=[]
        remainder=grid[0][0]%x
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                se.append(grid[i][j])
                if grid[i][j]%x!=remainder:
                    return -1


        se=sorted(se)
        right=len(se)
        value=se[right//2]

        print(value)
        count=0
        for i in se:
            if i!=value:
                count+=abs(i-value)//x
        
        return count


