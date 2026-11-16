class Solution:
    def convert(self, s: str, numRows: int) -> str:


        if numRows==1:
            return s 
            
        rows=[[""]*len(s) for i in range(numRows)]
        
        curr=[0,0]
        char=0
        directions=[0,1]

        while char<len(s):
           rows[curr[1]][curr[0]]=s[char]
           char+=1

           if directions==[0,1] and curr[1]==numRows-1:
                directions=[1,-1]
           elif directions==[1,-1] and curr[1]==0:
                directions=[0,1]
           
        
           curr[0]+=directions[0]
           curr[1]+=directions[1]
           print(curr)
        return "".join("".join(i) for i in rows)

        