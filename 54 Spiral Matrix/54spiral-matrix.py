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
        curr=(0,1)
        index=[0,0]
        while len(res)!=rows*columns:
            while 0<=index[0]+curr[0]<rows and 0<=index[1]+curr[1]<columns and matrix[index[0]+curr[0]][index[1]+curr[1]]>=-101:
                print(index)
                res.append(matrix[index[0]][index[1]])
                matrix[index[0]][index[1]]=-102
                index[0]+=curr[0]
                index[1]+=curr[1]
            res.append(matrix[index[0]][index[1]])
            matrix[index[0]][index[1]]=-102
            curr=direction_mp[curr]
            index[0]+=curr[0]
            index[1]+=curr[1]
        
        return res