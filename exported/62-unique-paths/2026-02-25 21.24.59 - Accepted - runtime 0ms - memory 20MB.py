class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mp={}
        def dfs(r,c):
            if r==m-1 and c==n-1:
                return 1
            elif r>=m or c>=n:
                return 0
            elif (r,c) in mp:
                return mp[(r,c)]
            else:
                temp=dfs(r+1,c)+dfs(r,c+1)
                mp[(r,c)]=temp
                return temp 

        return dfs(0,0)
