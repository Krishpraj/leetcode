class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        terminal=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="O" and (i==0 or i==len(board)-1 or j==0 or j==len(board[0])-1):
                    terminal.append((i,j))

        directions=[(0,1),(-1,0),(0,-1),(1,0)]  
        visited=set()
        res=[]
        def dfs(r,c):
            res.append((r,c))
            visited.add((r,c))
            for dr,dc in directions:
                if 0<=r+dr<len(board) and 0<=c+dc<len(board[0]) and board[r+dr][c+dc]=="O" and (r+dr,c+dc) not in visited:
                    dfs(r+dr,c+dc)
        
        for (i,j) in terminal:
            dfs(i,j)

        print(res)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) not in res: 
                    board[i][j]="X"
        
