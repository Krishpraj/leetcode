class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:



        product=1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                product=(product*grid[i][j])
        temp = [[product] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                temp[i][j]=(product//grid[i][j])%12345
        
        return temp
                




        class Solution:
            def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:

                m, n = len(grid), len(grid[0])
                temp = [[0]*n for _ in range(m)]

                prefix = 1
                for i in range(m):
                    for j in range(n):
                        temp[i][j] = prefix
                        prefix = (prefix * grid[i][j]) % 12345

                suffix = 1
                for i in range(m-1, -1, -1):
                    for j in range(n-1, -1, -1):
                        temp[i][j] = (temp[i][j] * suffix) % 12345
                        suffix = (suffix * grid[i][j]) % 12345

                return temp
        
