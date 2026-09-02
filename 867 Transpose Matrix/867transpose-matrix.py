class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
       

       matrix1=[[0]*len(matrix) for j in range(len(matrix[0]))]
       for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                matrix1[i][j]=matrix[j][i]
       return matrix1