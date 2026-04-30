class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        
        
        m=len(grid)
        n=len(grid[0])
        UNSET = None
        dp = [[[UNSET] * (k+1) for _ in range(n)] for _ in range(m)]


        def dfs(r,c,budget):
            
            if dp[r][c][budget] is not None:
                return dp[r][c][budget]

            cell_cost = 0 if grid[r][c] == 0 else 1
            cell_score=grid[r][c]

            if cell_cost>budget:
                return float('-inf')

            if r==m-1 and c==n-1:
                return cell_score

            down=dfs(r+1,c,budget-cell_cost) if r+1<m else float('-inf')
            right=dfs(r,c+1,budget-cell_cost) if c+1<n else float('-inf')
            
            res=max(down,right)+cell_score
            dp[r][c][budget]=res
            return res
    
        ans=dfs(0,0,k)
        if ans==float('-inf'):
            return -1
        else:
            return ans


        