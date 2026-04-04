class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, cols=len(board), len(board[0])

        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        
        visited=[]

        def dfs(i,j,idx):
            if board[i][j]==word[idx]:
                if idx==len(word)-1:
                    return True 
                else:
                    for dr,dc in directions:
                        if 0<=i+dr<rows and 0<=j+dc<cols and (i+dr,j+dc) not in visited:
                            visited.append((i,j))
                            if dfs(i+dr,j+dc,idx+1):
                                return True
                            visited.pop()


        for i in range(rows):
            for j in range(cols):
                if board[i][j]==word[0]:
                    if dfs(i,j,0):
                        return True 
        return False

    
        