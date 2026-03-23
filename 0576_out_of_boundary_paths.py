class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        mp={} # row columns and moves count came from that 
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(r,c,moves):
            if r>=m or c>=n or r<0 or c<0:
                return 1
            if moves==0:
                return 0
            if (r,c,moves) in mp:
                return mp[(r,c,moves)]

            count=0
            for dr,dc in directions:
                count+=dfs(r+dr,c+dc,moves-1)
            mp[(r,c,moves)]=count
            return count

        return dfs(startRow, startColumn, maxMove)%(10**9+7)
         
