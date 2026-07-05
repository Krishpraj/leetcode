class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:

        board = [[j for j in row] for row in board]
        mp={}
        def dfs(i,j): 
            print(i,j)
            if not 0<=i<len(board) or not 0<=j<len(board[0]):
                return (float("-inf"),0)
            if board[i][j]=="E":
                return (0,1)
            if board[i][j]=="X":
                return (float("-inf"),0)
            if (i,j) in mp: 
                return mp[(i,j)]
            else:
                p1=dfs(i-1,j)
                p2=dfs(i-1,j-1)
                p3=dfs(i,j-1)
                paths=0#prio maximum add paths from if 2 maximums are the same and mutliply by 2/3
                if p1[0]>=p2[0] and p1[0]>=p3[0]:
                    paths=p1[1]
                    if p1[0]==p2[0]:
                        paths+=p2[1]
                    if p1[0]==p3[0]:
                        paths+=p3[1]
                elif p2[0]>=p1[0] and p2[0]>=p3[0]:
                    paths=p2[1]
                    if p1[0]==p2[0]:
                        paths+=p1[1]
                    if p2[0]==p3[0]:
                        paths+=p3[1]
                elif p3[0]>=p1[0] and p3[0]>=p2[0]:
                    paths=p3[1]
                    if p3[0]==p2[0]:
                        paths+=p2[1]
                    if p1[0]==p3[0]:
                        paths+=p1[1]

                mp[(i,j)]=(max(p1[0],p2[0],p3[0])+int(board[i][j]),paths)
                return mp[(i,j)]
        board[-1][-1]=0
        ans=dfs(len(board)-1,len(board[0])-1)
    
        if ans[0]==float("-inf"):
            return (0,0)
        else: 
            return (ans[0],ans[1]%(10**9 + 7)) 