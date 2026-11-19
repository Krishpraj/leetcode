class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        
        max_columns=[float("-inf")]*len(matrix[0])
        min_rows=[float("inf")]*len(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_columns[j]=max(max_columns[j],matrix[i][j])
                min_rows[i]=min(min_rows[i],matrix[i][j])

        res=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==max_columns[j]==min_rows[i]:
                    res.append(matrix[i][j])
        
        return res 
