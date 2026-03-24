class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res=False
        directions=[[0,1],[-1,0],[0,-1],[1,0]]
        visited=set()

        
        def dfs(r,c,i:int):
            nonlocal res

            if i==len(word):
                res=True
                return
            for dr,dc in directions:
                if 0<=r+dr and r+dr<len(board) and 0<=c+dc and c+dc<len(board[0]) and tuple([r+dr,c+dc]) not in visited:
                    if board[r+dr][c+dc]==word[i]:
                        visited.add(tuple([r+dr,c+dc]))
                        dfs(r+dr,c+dc,i+1)
                        visited.remove(tuple([r+dr,c+dc]))
                        

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    visited.add(tuple([i,j]))
                    dfs(i,j,1)
                    visited.remove(tuple([i,j]))
                    if res==True:
                        return True 
        
        return False
        