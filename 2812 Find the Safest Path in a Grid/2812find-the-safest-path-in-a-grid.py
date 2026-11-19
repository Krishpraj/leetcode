class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        
        directions=[[0,1],[-1,0],[0,-1],[1,0]]
        
        g=[[-1]*len(grid[0]) for i in range(len(grid))]
        t=deque()

        def bfs():
            mx=0
            while t:
                r,c=t.popleft()
                for dr,dc in directions: 
                    if 0<=r+dr<len(grid) and 0<=c+dc<len(grid[0]) and g[r+dr][c+dc]==-1:
                        g[r+dr][c+dc]=g[r][c]+1
                        mx=max(mx,g[r][c]+1)
                        t.append((r+dr,c+dc))
            return mx
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    g[i][j]=0
                    t.append((i,j))
      
        def safe(v):
            if g[0][0] < v or g[-1][-1] < v:
                return False
            visited = [[False] * len(grid[0]) for _ in range(len(grid))]
            d = deque()
            d.append((0, 0))
            visited[0][0] = True
            while d:
                r, c = d.popleft()
                if r == len(grid)-1 and c == len(grid[0])-1:
                    return True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and g[nr][nc] >= v and not visited[nr][nc]):
                        visited[nr][nc] = True
                        d.append((nr, nc))
            return False

        r=bfs()
        print(g)
        l=0
        res=0
        while l<=r:
            mid=(l+r)//2
            
            if safe(mid):
                res=mid
                l=mid+1
            else:
                r=mid-1
        return res

        















        