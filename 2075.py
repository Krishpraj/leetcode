class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:

        lenrow=len(encodedText)//rows

        res=[]
        ans=[]
        for i in range(len(encodedText)):
            ans.append(encodedText[i])
            if len(ans)==lenrow:
                res.append(ans[:])
                ans=[]

        if not res:
            return ""
        
        original=""
        for i in range(len(res[0])):
            for j in range(rows):
                if i+j<lenrow:
                    original=original+res[j][i+j]

        return original.rstrip()


    
