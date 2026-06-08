class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        
        memarray = {} 

        def dfs(r,c): 

            if (r, c)  in memarray:
                return memarray[(r, c)]
            curr=matrix[r][c]

            max_result = 1
            for dr,dc in directions: 
                if 0<=r+dr<len(matrix) and 0<=c+dc<len(matrix[0]) and matrix[r+dr][c+dc]>matrix[r][c]:
                    max_result = max(max_result, 1 + dfs(r+dr,c+dc))

            memarray[(r, c)]  = max_result
            return max_result

        maxlen = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
               maxlen = max(maxlen, dfs(i,j))
        
        return maxlen