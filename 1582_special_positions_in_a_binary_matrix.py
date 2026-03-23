ass Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        

        contending_rows=[]
        for i in range(len(mat)): # rows with only 1 ones we list donw columns 
            res=[] 
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    res.append(j)
            if len(res)==1:
                contending_rows.append(res[0])

        print(contending_rows)
        count=0
        for i in contending_rows: #columns
            counted_rows=0
            for j in range(len(mat)):
                if mat[j][i]==1:
                    counted_rows+=1
                    print(j,i)
            
            if counted_rows==1:
                count+=1
        
        return count
