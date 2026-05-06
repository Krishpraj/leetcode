class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:


        for arr in range(len(boxGrid)):
            i=len(boxGrid[0])-1
            last=len(boxGrid[0])
            while i>=0:
           
                if boxGrid[arr][i]=="#":
                    boxGrid[arr][i]="."
                    boxGrid[arr][last-1]="#"                    
                    last-=1
                elif boxGrid[arr][i]=="*":
                    last=i
                i-=1
      

        boxGrid=boxGrid[::-1]
        # rows
        m = len(boxGrid)
        # cols
        n=len(boxGrid[0])
        res = [[0] * m for _ in range(n)]
        for i in range(len(boxGrid)):
            for j in range(len(boxGrid[0])):
                res[j][i]=boxGrid[i][j]
        
        return res
                

            
                    

            
    