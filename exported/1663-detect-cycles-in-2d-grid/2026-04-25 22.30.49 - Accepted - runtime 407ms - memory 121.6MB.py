class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c, pr, pc):
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == grid[r][c]:
                    
                    # don't go back to parent
                    if (nr, nc) == (pr, pc):
                        continue

                    # cycle found
                    if (nr, nc) in visited:
                        return True

                    if dfs(nr, nc, r, c):
                        return True

            return False

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited:
                    if dfs(i, j, -1, -1):
                        return True

        return False

