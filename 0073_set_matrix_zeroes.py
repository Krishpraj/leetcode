class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=[]
        columns=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    rows.append(i)
                    columns.append(j)  


        print(rows,columns)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows:
                    matrix[i][j]=0
                if j in columns:
                    matrix[i][j]=0

    
