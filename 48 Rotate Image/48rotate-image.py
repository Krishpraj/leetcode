class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        mp={}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                c=len(matrix)-1-i
                r=j
                mp[(r,c)]=matrix[i][j]

        print(mp)
        for i,v in mp.items():
            matrix[i[0]][i[1]]=v
        
        
    

        
    