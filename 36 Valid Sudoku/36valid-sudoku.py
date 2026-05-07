class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        for i in range(len(board)):
            list1 = []
            list2 = []

            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue

                if board[i][j] in list1:
                    return False
                
                list1.append(board[i][j])
        
            for j in range(len(board[0])):
                if board[j][i] == ".":
                    continue
                    
                if board[j][i] in list2:
                    print("col")
                    return False
                
                list2.append(board[j][i])

        for i in range(3):
            for j in range(3):
                list1 = []

                for k in range(3):
                    for l in range(3):

                        if board[i*3 + k][j*3 + l] == ".":
                            continue

                        if board[i* 3 + k][j*3 + l] in list1:
                            print("3")
                            return False
                        list1.append(board[i*3 + k][j*3 + l])

        return True

            # check rows

            # checck cols
            