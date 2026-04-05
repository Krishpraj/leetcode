class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        arr=[]
        for i in range(1,n**2+1,n):
            arr.append([0 for j in range(i,i+n)])

        direction_mp = {
            (0, 1): (1, 0),    # right -> down
            (1, 0): (0, -1),   # down -> left
            (0, -1): (-1, 0),  # left -> up
            (-1, 0): (0, 1)    # up -> right
        }


        i=0
        j=0
        dr,dc=0,1
        count=1
        visited=[]

        

        while len(visited)!=n**2:
            arr[i][j]=count
            count+=1
            visited.append((i,j))

            if not 0<=i+dr<len(arr)  or not 0<=j+dc<len(arr[0]) or (i+dr,j+dc) in visited :
                x=direction_mp[(dr,dc)]
                dr=x[0]
                dc=x[1]

            i=i+dr
            j=j+dc
            
        return arr
