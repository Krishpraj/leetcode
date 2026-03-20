class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        x=bin(n)
        res=[]
        for i in x[2:]:
            print(i)
            if i=="0":
                res.append("1")  
            else:
                res.append("0")
    
            
        print(res)
        
        res="".join(res)
        print(res)
        y= int(res,2)

        return y  

