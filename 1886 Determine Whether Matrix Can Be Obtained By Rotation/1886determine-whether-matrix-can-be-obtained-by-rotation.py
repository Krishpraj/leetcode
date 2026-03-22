class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        

        # rotate 4 times

        count=0
        
        while count!=4:
            temp=[[0]*len(mat) for i in range(len(mat))]
           
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    temp[i][j]=mat[j][len(mat)-i-1]
            
            mat=temp
            count+=1
            if temp==target:
                return True 
        
        return False


