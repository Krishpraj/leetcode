class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        rows, columns=len(matrix), len(matrix[0])
        direction_mp = {
            (0, 1): (1, 0),    # right -> down
            (1, 0): (0, -1),   # down -> left
            (0, -1): (-1, 0),  # left -> up
            (-1, 0): (0, 1)    # up -> right
        }
        res=[]
        curr=(0,1) ## direction 
        index=[0,0] ## cell 
        while len(res)!=rows*columns:
            res.append(matrix[index[0]][index[1]])
            matrix[index[0]][index[1]]=-102
            if 0<=index[0]+curr[0]<rows and 0<=index[1]+curr[1]<columns and matrix[index[0]+curr[0]][index[1]+curr[1]]>=-101:
                index[0]+=curr[0]
                index[1]+=curr[1] 
            else:
                curr=direction_mp[curr]
                index[0]+=curr[0]
                index[1]+=curr[1] 
        
        return res
